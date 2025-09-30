# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 09:07:40 2022

@author: janpe
"""

from .fancy_classes import Graph
from .saver import saver
from .lossfunctions import loss_dic
import numpy as np
from scipy import optimize
import json

import logging

log = logging.getLogger(__name__)


class topological_opti:

    def __init__(self, start_graph: Graph, saver: saver, ent_dic=None, target_state=None,
                 config=None, safe_history=True):

        #print(f"Hallo Soeren! topological_opti __init__ 1")
        self.config = config
        #print(f"Hallo Soeren! topological_opti __init__ 2")
        self.imaginary = self.config['imaginary']
        #print(f"Hallo Soeren! topological_opti __init__ 3, self.config['loss_func']={self.config['loss_func']}")
        if self.config['loss_func'] == 'ent':
            self.ent_dic = ent_dic
        else:
            self.target = target_state  # object of State class
        #print(f"Hallo Soeren! topological_opti __init__ 4")

        # do preoptimization on complete starting graph, this might already take some time
        self.graph = self.pre_optimize_start_graph(start_graph)
        #print(f"Hallo Soeren! topological_opti __init__ 5")
        self.saver = saver
        #print(f"Hallo Soeren! topological_opti __init__ 6")
        self.save_hist = safe_history
        #print(f"Hallo Soeren! topological_opti __init__ 7")
        self.history = []

    def check(self, result: object, lossfunctions: object):
        """
        check if all loss functions fulfill conditions for success. mostly defined through thresholds.

        Parameters
        ----------
        result : object
             from scipy.mimnimizer class
        lossfunctions : object
            list of all loss functions

        Returns
        -------
        bool
            False if we keep Graph or True if we can delete edge

        """

        if self.config['loss_func'] == 'ent':
            if abs(result.fun) - abs(self.loss_val[0]) > self.config['thresholds'][0]:
                return False
        else:
            # uncomment to see where checks fail
            # print(result.fun, self.config['thresholds'][0])
            if result.fun > self.config['thresholds'][0]:
                # if check fails return false
                print(f"    inside self.check1: result.fun={result.fun}, self.config['thresholds'][0]={self.config['thresholds'][0]}")
                return False
            # check if all loss functions are under the corresponding threshold
            for ii in range(1, len(lossfunctions)):
                if lossfunctions[ii](result.x) > self.config['thresholds'][ii]:
                    # if check fails return false
                    print(f"    inside self.check2: ii={ii}, lossfunctions[ii](result.x)={lossfunctions[ii](result.x)}, self.config['thresholds'][ii]={self.config['thresholds'][ii]}")
                    return False
        # when no check fails return True  = success
        return True

    def weights_to_valid_input(self, weights: list) -> list:
        """
        need to change weights from scip optimizer to proper input 
        if one optimize with complexe values

        Parameters
        ----------
        weights : list
            list of weights

        Raises
        ------
        ValueError
            if imaginary is not defined correctly in config file

        Returns
        -------
        list
            ordered list according to imaginary

        """
        if self.imaginary == 'cartesian':

            if len(weights) % 2 == 0:
                ll2 = int(len(weights) / 2)
            else:
                raise ValueError(
                    'odd number of weights for complex optimization')

            return [complex(real, imag) for real, imag in
                    zip(weights[:ll2], weights[ll2:])]

        elif self.imaginary == 'polar':

            if len(weights) % 2 == 0:
                ll2 = int(len(weights) / 2)
            else:
                raise ValueError(
                    'odd number of weights for complex optimization')
            return [(radius, phase) for radius, phase in
                    zip(weights[:ll2], weights[ll2:])]
        elif self.imaginary is False:
            return weights
        else:
            raise ValueError('imaginary: only: polar,cartesian,false')

    def get_loss_functions(self, current_graph: Graph):
        """
        get a list of all loss functions mentioned in config

        Parameters
        ----------
        current_graph

        Returns
        -------
        callable_loss
            list of callable functions

        """
        # get loss function acc. to config
        
        print("hi soeren, get_loss_functions1")
        
        lossfunctions = loss_dic[self.config['loss_func']]
        
        print(f"hi soeren, get_loss_functions2: {self.config['loss_func']}")

        # entanglement loss function
        if self.config['loss_func'] == 'ent':  # we optimize for entanglement
            loss_specs = {'sys_dict': self.ent_dic,
                          'imaginary': self.imaginary,
                          'var_factor': self.config['var_factor']}


        # CR and FID
        elif self.config['loss_func'] in ['cr', 'fid']:
            print(f"hi soeren, get_loss_functions3")            
            loss_specs = {'target_state': self.target,
                          'cnfg': self.config}
            print(f"hi soeren, get_loss_functions4")   

        # fock basis
        elif self.config['loss_func'] in ['fockcr', 'fockfid']:
            # loss_specs = {'target_state': self.target,
            #              'cnfg': self.config}
            loss_specs = {'target_state': self.target,
                          'num_anc': self.config['num_anc'],
                          'amplitudes': self.config['amplitudes'],
                          'imaginary': self.imaginary}

        # custom loss functions
        elif self.config['loss_func'] == 'lff':
            loss_specs = {'cnfg': self.config}
            
            
        print(f"hi soeren, get_loss_functions4.5")   
        print(f"    lossfunctions: {len(lossfunctions)}")
            
        callable_loss = [func(current_graph, **loss_specs)
                         for func in lossfunctions]

        print(f"hi soeren, get_loss_functions5")           
        
        if 'thresholds' not in self.config:
            raise ValueError(f'thresholds not defined in config file. Please define thresholds as list of floats (length = {len(callable_loss)}).')
        
        print(f"hi soeren, get_loss_functions6")
                
        
        testinit, _ = self.prepOptimizer(len(current_graph))

        print(f"hi soeren, get_loss_functions7")        
        for loss in callable_loss:
            loss(testinit)
        return callable_loss

    def update_losses(self, result, losses):
        """
        updates the losses for next steps

        Parameters
        ----------
        result : scipy.minimizer object
            minimize object from optimizaiton step
        losses : list
            list of loss functions

        Returns
        -------
        list of losses for corrosponding weights stored in result.x

        """
        loss_values = [result.fun]
        for ii in range(1, len(losses)):
            loss_values.append(losses[ii](result.x))
        return loss_values

    class LossLogger:
        def __init__(self, loss_fn):
            self.loss_fn = loss_fn
            self.nfev = 0
            self.last_f = None  # optional, to share with a callback
    
        def __call__(self, x):
            f = self.loss_fn(x)
            self.nfev += 1
            self.last_f = f
            if self.nfev % 50 ==0:
                print(f"[feval {self.nfev:4d}] f = {float(f):.8f}")
            return f

    def pre_optimize_start_graph(self, graph) -> Graph:
        """
        first optimization of complete starting graph

        Parameters
        ----------
        graph

        Returns
        -------
        preopt_graph

        """
        # losses is a list of callable lossfunctions, e.g. [countrate(x), fidelity(x)], where x is a vector of edge weights
        # that can be given to scipy.optimize
        
        print("hi soeren! here we go pre_optimize_start_graph1")
        
        log.info('loading losses')
        losses = self.get_loss_functions(graph)
        log.info('losses done')
        valid = False
        counter = 0
        print("hi soeren! here we go pre_optimize_start_graph2")
        # repeat optimization of complete graph until a good solution is found (which satifies self.check())
        while not valid:
            # prepare optimizer
            initial_values, bounds = self.prepOptimizer(len(graph))
            #print("hi soeren! here we go pre_optimize_start_graph, in while1")
            # optimization with scipy
            log.info('begin preopt')
            print(f'    len(initial_values)={len(initial_values)}')
            print(f'    initial_values={initial_values[0:10]}')
            print(f'    bounds={bounds}')
            #print("hi soeren! here we go pre_optimize_start_graph, in while2")
            #best_result = optimize.minimize(losses[0], x0=initial_values,
            #                                bounds=bounds,
            #                                method=self.config['optimizer'],
            #                                options={'ftol': self.config['ftol']})
            
            obj = self.LossLogger(losses[0])  # or every=10 to reduce spam
            best_result = optimize.minimize(
                obj, x0=initial_values, bounds=bounds,
                method='L-BFGS-B',
                options={'ftol': 1e-6, 'gtol': 1e-8, 'maxiter': 1000000, 'maxfun': 1000000, 'disp': True}
            )            
            
            print(f'    best_result={best_result}')
            #print("hi soeren! here we go pre_optimize_start_graph, in while3")
            log.info('end preopt')
            #print("hi soeren! here we go pre_optimize_start_graph, in while4")
            self.loss_val = self.update_losses(best_result, losses)
            #print("hi soeren! here we go pre_optimize_start_graph, in while5")
            # check if solution is valid
            valid = self.check(best_result, losses)
            #print("hi soeren! here we go pre_optimize_start_graph, in while6")
            counter += 1
            # print a warning if preoptimization is stuck in a loop
            if counter % 10 == 0:
                #print('10 invalid preoptimization, consider changing parameters.')
                log.info('10 invalid preoptimization, consider changing parameters.')
            if counter % 100 == 0:
                #print('100 invalid preoptimization, state cannot be found.')
                log.info('100 invalid preoptimization, state cannot be found.')
                raise ValueError('100 invalid preoptimization steps. Conclusion: State cannot be created with provides parameters. Consider adding more ancillas or using less restrictions if possible (e.g. removed_connections).')
        #print("hi soeren! here we go pre_optimize_start_graph ourside while 1")
        # if num_pre is set to larger than 1 in config, do num_pre preoptimization and choose the best one.
        # for optimizations with concrete target state, num_pre = 1 is enough
        for __ in range(self.config['num_pre'] - 1):
            initial_values, bounds = self.prepOptimizer(len(graph))
            obj = self.LossLogger(losses[0])  # or every=10 to reduce spam
            result = optimize.minimize(
                obj, x0=initial_values, bounds=bounds,
                method='L-BFGS-B',
                options={'ftol': 1e-6, 'gtol': 1e-8, 'maxiter': 1000000, 'maxfun': 1000000, 'disp': True}
            )     

            if result.fun < best_result.fun:
                best_result = result
        print("hi soeren! here we go pre_optimize_start_graph ourside for 1")
        self.loss_val = self.update_losses(best_result, losses)
        print(f'best result from pre-opt: {abs(best_result.fun)}')
        log.info(f'best result from pre-opt: {abs(best_result.fun)}')

        for ii, edge in enumerate(graph.edges):
            graph[edge] = best_result.x[ii]
        preopt_graph = graph.copy()

        try:
            bulk_thr = self.config['bulk_thr']
        except:
            bulk_thr = 0
        if bulk_thr > 0:
            # cut all edges smaller than bulk_thr and optimize again
            # this can save a lot of time
            cont = True
            num_deleted = 0
            while cont:
                # delete smallest edges one by one
                min_edge = preopt_graph.minimum()
                amplitude = preopt_graph[min_edge]
                if self.imaginary == 'polar':
                    amplitude = amplitude[0]
                if abs(amplitude) < bulk_thr:
                    preopt_graph.remove(min_edge, update=True)
                    num_deleted += 1
                else:
                    cont = False
            print(f'{num_deleted} edges deleted')
            log.info(f'{num_deleted} edges deleted')
            valid = False
            while not valid:
                # it is necessary that the truncated graph passes the checks
                initial_values, bounds = self.prepOptimizer(len(preopt_graph))
                losses = self.get_loss_functions(preopt_graph)
                trunc_result = optimize.minimize(losses[0], x0=initial_values,
                                                 bounds=bounds,
                                                 method=self.config['optimizer'],
                                                 options={'ftol': self.config['ftol']})
                self.loss_val = self.update_losses(trunc_result, losses)
                print(f'result after truncation: {abs(trunc_result.fun)}')
                log.info(f'result after truncation: {abs(trunc_result.fun)}')
                valid = self.check(trunc_result, losses)
        
            for ii, edge in enumerate(preopt_graph.edges):
                preopt_graph[edge] = trunc_result.x[ii]

        return preopt_graph

    def prepOptimizer(self, numweights, x=[]):
        """
        returns initial values and bounds for use in optimization.

        Parameters
        ----------
        numweights
        x

        Returns
        -------
        initial_values
        bounds
        """

        if not self.imaginary:
            bounds = numweights * [(-1, 1)]
            if len(x) == 0:
                initial_values = 2 * np.random.random(numweights) - 1
            else:
                initial_values = x
        else:
            bounds = numweights * [(-1, 1)] + numweights * [(-np.pi, np.pi)]
            if len(x) == 0:
                rands_r = 2 * np.random.random(numweights) - 1
                rands_th = 2 * np.pi * np.random.random(numweights) - np.pi
                initial_values = np.concatenate([rands_r, rands_th])
            else:
                initial_values = x

        return initial_values, bounds

    def continuationCondition(self, num_edge) -> bool:
        """
        conditions that stop optimization

        Parameters
        ----------
        num_edge

        Returns
        -------
        cont: bool
            if True, topological optimization is continued
        """
        if self.config['loss_func'] == 'ent':
            cont = len(self.graph) > self.config['min_edge'] and num_edge < len(
                self.graph)
        else:
            # if num_edge is higher than total number of edges in the graph
            # or higher than edges_tried, return False
            cont = num_edge < min(len(self.graph), self.config['edges_tried'])
        return cont

    def optimize_one_edge(self, num_edge: int,
                          num_tries_one_edge: int) -> (Graph, bool):
        """
        delete the num_edge-th smallest edge and optimize num_tries_one_edge times
        and check if corresponding loss function fulfills checks

        Parameters
        ----------
        num_edge
        num_tries_one_edge

        Returns
        -------
        new_graph
           if edge is successfully deleted, reduced graph is returned. else graph is not modified.
        success
        """
        
        print("hi soeren, optimize_one_edge1")
        
        # copy current Graph and delete num_edge´s smallest weight
        # set up reduced graph
        reduced_graph = self.graph.copy()
        # find index of num_edge smallest edge
        min_edge = reduced_graph.minimum(num_edge)
        # store amplitude in case edge fails and needs to be put back in
        amplitude = reduced_graph[min_edge]
        # remove smallest edge
        reduced_graph.remove(min_edge, update=True)
        
        print("hi soeren, optimize_one_edge2")
        # try a given number of times to delete this edge
        for ii in range(num_tries_one_edge):
            # if edge is tried for the first time, update loss function and other optimization parameters
            # also the weights of the old graph are used as initial values (this is much faster)
            if ii == 0:
                try:
                    # redefine loss functions for reduced graph
                    losses = self.get_loss_functions(reduced_graph)
                    # use initial values x0 from previous Graph
                    x0 = reduced_graph.weights
                    initial_values, bounds = self.prepOptimizer(len(reduced_graph),
                                                                x=x0)
                    # optimize with scipy
                    result = optimize.minimize(losses[0], x0=initial_values,
                                               bounds=bounds,
                                               method=self.config['optimizer'],
                                               options={'ftol': self.config['ftol']})
                except Exception as e:
                    # if the target kets can not be produced with the given graph we can give up on this edge
                    # it wont work
                    reduced_graph[min_edge] = amplitude
                    print('edge necessary for producing all kets')
                    log.info('edge necessary for producing all kets')
                    return reduced_graph, False  # no success keep current Graph
            # if edge has been tried before, reuse loss function etc. and use random initial values
            else:
                # random initial values
                initial_values, bounds = self.prepOptimizer(len(reduced_graph))
                # optimize with scipy
                result = optimize.minimize(losses[0], x0=initial_values,
                                           bounds=bounds,
                                           method=self.config['optimizer'],
                                           options={'ftol': self.config['ftol']})
            # check if solution is valid
            valid = self.check(result, losses)
            
            print("hi soeren, optimize_one_edge3")

            if valid:  # if criterion is reached then save reduced graph as graph, else leave graph as is
                # compute values for all losses
                self.loss_val = self.update_losses(result, losses)
                # if clean solution is encountered before optimization finishes, save that too
                # all weights are +-1 and solution is pretty good, it is interesting enough to be saved
                # to a file even if topological optimization can be continued
                if all(np.array(abs(self.graph)) > 0.95):
                    self.saver.save_graph(self)
                if self.save_hist:
                    self.history.append([str(self.graph),self.loss_val])
                # return updated result graph
                result_graph = reduced_graph.copy()
                for ii, edge in enumerate(reduced_graph.edges):
                    result_graph[edge] = result.x[ii]
                return result_graph, True
        # all tries failed keep current Graph
        reduced_graph[min_edge] = amplitude
        return reduced_graph, False

    def topologicalOptimization(self, save_hist=True) -> Graph:
        """
        does the topological main loop. deletes edges until continuation condition fails.
        Returns
        -------
        solution_graph
            result of optimization
        """
        # start with smallest edge
        num_edge = 0
        graph_history = []
        print("hi soeren, in topologicalOptimization1")
        # if num_edge becomes too large, optimization is stopped
        cc=0
        while self.continuationCondition(num_edge):
            # try if num_edge smallest edge can be removed
            # if successful, return optimized graph after deletion
            # if not successful, return old graph
            print(f"hi soeren, in topologicalOptimization2: {cc}")
            self.graph, success = self.optimize_one_edge(
                num_edge, self.config['tries_per_edge'])
            print(f"hi soeren, in topologicalOptimization3: {cc}")
            # iterate num_edge to try next smallest edge
            num_edge += 1
            log.info(f'deleting edge {num_edge}')
            print(f'deleting edge {num_edge}')
            if success:
                print(
                    f"deleted: {len(self.graph)}  edges left with loss {self.loss_val[0]:.3f}")
                log.info(f"deleted: {len(self.graph)}  edges left with loss {self.loss_val[0]:.3f}")
                # reset to try smallest edge again for next iteration
                num_edge = 0
                graph_history.append(self.graph)

        return self.graph
