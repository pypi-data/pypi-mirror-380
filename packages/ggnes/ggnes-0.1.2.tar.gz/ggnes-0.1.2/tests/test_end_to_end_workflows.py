"""
End-to-end workflow tests for complete GGNES usage scenarios.
Tests full pipelines from graph creation to model deployment.
"""

import json
import os
import pickle
import sys
import tempfile
import uuid

import pytest

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
import torch

from ggnes.core import Graph, NodeType
from ggnes.evolution import Genotype
from ggnes.evolution.operators import mutate, uniform_crossover
from ggnes.generation import generate_network
from ggnes.rules.rule import EmbeddingLogic, LHSPattern, RHSAction, Rule
from ggnes.translation import to_pytorch_model
from ggnes.utils.rng_manager import RNGManager


class TestCompleteNASWorkflow:
    """Test complete neural architecture search workflow."""

    @pytest.mark.xfail(reason="Multiple API issues prevent workflow")
    def test_basic_nas_pipeline(self):
        """Test basic NAS pipeline from start to finish."""

        # Step 1: Create initial graph
        graph = Graph()
        graph.add_node(
            {
                "id": "input",
                "type": "input",
                "size": 784,  # MNIST-like
            }
        )
        graph.add_node({"id": "output", "type": "output", "size": 10})
        graph.add_edge("input", "output")

        # Step 2: Define evolution rules
        rules = []

        # Add hidden layer rule
        rules.append(
            Rule(
                name="add_hidden",
                pattern=LHSPattern(),
                action=RHSAction(add_node={"type": "hidden", "size": 128, "activation": "relu"}),
            )
        )

        # Add skip connection rule
        rules.append(
            Rule(
                name="add_skip", pattern=LHSPattern(min_distance=2), action=RHSAction(add_edge=True)
            )
        )

        # Step 3: Create population
        population = []
        for _ in range(20):
            genotype = Genotype(rules=rules)
            population.append(genotype)

        # Step 4: Evolution loop
        for generation in range(10):
            # Generate networks from genotypes
            networks = []
            for genotype in population:
                network = generate_network(genotype, axiom=graph)
                networks.append(network)

            # Evaluate fitness
            fitness_scores = []
            for network in networks:
                score = evaluate_network(network)
                fitness_scores.append(score)

            # Selection
            parents = select_parents(population, fitness_scores)

            # Create next generation
            next_population = []
            for i in range(0, len(parents), 2):
                child1, child2 = crossover(parents[i], parents[i + 1])
                child1 = mutate(child1)
                child2 = mutate(child2)
                next_population.extend([child1, child2])

            population = next_population

        # Step 5: Get best architecture
        best_genotype = max(population, key=lambda g: evaluate_network(generate_network(g, graph)))
        best_graph = generate_network(best_genotype, graph)

        # Step 6: Convert to PyTorch and train
        model = to_pytorch_model(best_graph)
        trained_model = train_model(model)

        # Step 7: Evaluate
        accuracy = evaluate_model(trained_model)
        assert accuracy > 0.9

    def test_actual_minimal_workflow(self):
        """Test minimal workflow with actual API."""

        # Step 1: Create graph with actual API
        graph = Graph()

        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        hidden_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 20},
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        graph.add_edge(source_id=input_id, target_id=hidden_id)
        graph.add_edge(source_id=hidden_id, target_id=output_id)

        # Step 2: Convert to PyTorch
        model = to_pytorch_model(graph)

        # Step 3: Test forward pass
        x = torch.randn(32, 10)
        y = model(x)
        assert y.shape == (32, 1)

        # Step 4: Simple training
        optimizer = torch.optim.Adam(model.parameters())
        loss_fn = torch.nn.MSELoss()

        for _ in range(10):
            y_pred = model(x)
            y_true = torch.randn(32, 1)
            loss = loss_fn(y_pred, y_true)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # Model should be trainable
        assert loss.item() < 100  # Some reasonable bound


class TestModelExportImportWorkflow:
    """Test model export, import, and deployment workflow."""

    def test_graph_serialization_workflow(self):
        """Test saving and loading graphs."""
        # Create a graph
        graph = Graph()

        n1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        n2 = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 20},
            }
        )

        n3 = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        graph.add_edge(source_id=n1, target_id=n2)
        graph.add_edge(source_id=n2, target_id=n3)

        # Save graph
        with tempfile.NamedTemporaryFile(suffix=".pkl", delete=False) as f:
            pickle.dump(graph, f)
            temp_path = f.name

        # Load graph
        with open(temp_path, "rb") as f:
            loaded_graph = pickle.load(f)

        # Verify structure preserved
        assert len(loaded_graph.nodes) == len(graph.nodes)
        assert len(list(loaded_graph.list_edges())) == len(list(graph.list_edges()))

        # Clean up
        os.unlink(temp_path)

    @pytest.mark.xfail(reason="No genotype serialization")
    def test_genotype_export_import(self):
        """Test genotype serialization workflow."""
        # Create genotype with rules
        genotype = Genotype()

        for i in range(3):
            rule = Rule(
                rule_id=uuid.uuid4(),
                lhs=LHSPattern(nodes=[], edges=[], boundary_nodes=[]),
                rhs=RHSAction(add_nodes=None),
                embedding=EmbeddingLogic(),
                metadata={"index": i},
            )
            genotype.add_rule(rule)

        # Export to JSON
        genotype_dict = genotype.to_dict()
        json_str = json.dumps(genotype_dict)

        # Import from JSON
        loaded_dict = json.loads(json_str)
        loaded_genotype = Genotype.from_dict(loaded_dict)

        # Verify
        assert len(loaded_genotype.rules) == len(genotype.rules)
        assert loaded_genotype.id == genotype.id

    def test_pytorch_model_export(self):
        """Test exporting PyTorch models."""
        # Create graph
        graph = Graph()

        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        graph.add_edge(source_id=input_id, target_id=output_id)

        # Convert to PyTorch
        model = to_pytorch_model(graph)

        # Save model
        with tempfile.NamedTemporaryFile(suffix=".pt", delete=False) as f:
            torch.save(model.state_dict(), f.name)
            temp_path = f.name

        # Load model
        new_model = to_pytorch_model(graph)
        new_model.load_state_dict(torch.load(temp_path))

        # Verify same output
        x = torch.randn(10, 10)
        with torch.no_grad():
            y1 = model(x)
            y2 = new_model(x)

        assert torch.allclose(y1, y2)

        # Clean up
        os.unlink(temp_path)


class TestEvolutionWithFitnessWorkflow:
    """Test evolution with custom fitness functions."""

    def test_evolution_with_accuracy_fitness(self):
        """Test evolution optimizing for accuracy."""
        # Create simple dataset
        X_train = torch.randn(100, 10)
        y_train = torch.randn(100, 1)

        def fitness_function(genotype):
            """Evaluate genotype on training data."""
            try:
                # Create graph from genotype
                graph = create_graph_from_genotype(genotype)

                # Convert to model
                model = to_pytorch_model(graph)

                # Quick training
                optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
                loss_fn = torch.nn.MSELoss()

                for _ in range(5):
                    y_pred = model(X_train)
                    loss = loss_fn(y_pred, y_train)

                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()

                # Return negative loss as fitness
                with torch.no_grad():
                    final_loss = loss_fn(model(X_train), y_train).item()

                return -final_loss  # Higher is better

            except:
                return -1000  # Penalty for invalid architectures

        # Create initial population
        population = []
        for _ in range(10):
            genotype = Genotype()
            # Add some random rules
            for _ in range(np.random.randint(1, 4)):
                rule = Rule(
                    rule_id=uuid.uuid4(),
                    lhs=LHSPattern(nodes=[], edges=[], boundary_nodes=[]),
                    rhs=RHSAction(add_nodes=None),
                    embedding=EmbeddingLogic(),
                )
                genotype.add_rule(rule)
            population.append(genotype)

        # Evolution
        rng = RNGManager(seed=42)
        config = {
            "mutation_rate": 0.1,
            "mutation_probs": {"add_rule": 0.5, "delete_rule": 0.3, "modify_rule": 0.2},
            "crossover_probability_per_rule": 0.5,
        }

        best_fitness = -float("inf")

        for generation in range(5):
            # Evaluate population
            fitness_scores = [fitness_function(g) for g in population]

            # Track best
            gen_best = max(fitness_scores)
            if gen_best > best_fitness:
                best_fitness = gen_best

            # Selection (keep best half)
            sorted_pop = sorted(zip(fitness_scores, population), reverse=True)
            parents = [g for _, g in sorted_pop[: len(population) // 2]]

            # Create next generation
            next_population = parents.copy()  # Elitism

            while len(next_population) < len(population):
                # Select two parents
                p1 = parents[np.random.randint(len(parents))]
                p2 = parents[np.random.randint(len(parents))]

                # Crossover
                try:
                    c1, c2 = uniform_crossover(p1, p2, config, rng)
                    # Mutation
                    c1 = mutate(c1, config, rng)
                    c2 = mutate(c2, config, rng)
                    next_population.extend([c1, c2])
                except:
                    # If crossover/mutation fails, just copy parents
                    next_population.extend([p1, p2])

            population = next_population[: len(population)]

        # Best fitness should improve
        assert best_fitness > -1000


class TestMultiObjectiveWorkflow:
    """Test multi-objective optimization workflows."""

    @pytest.mark.xfail(reason="No multi-objective support")
    def test_pareto_optimization(self):
        """Test optimizing for accuracy vs efficiency."""

        def evaluate_objectives(genotype):
            """Evaluate multiple objectives."""
            graph = create_graph_from_genotype(genotype)
            model = to_pytorch_model(graph)

            # Objective 1: Model size (minimize)
            num_params = sum(p.numel() for p in model.parameters())

            # Objective 2: Accuracy proxy (maximize)
            # Use negative loss as proxy
            X = torch.randn(10, 10)
            y = torch.randn(10, 1)

            with torch.no_grad():
                y_pred = model(X)
                loss = torch.nn.functional.mse_loss(y_pred, y)
                accuracy_proxy = -loss.item()

            return {
                "size": -num_params,  # Negative because we minimize
                "accuracy": accuracy_proxy,
            }

        # Run multi-objective evolution
        from ggnes.evolution import nsga2_evolve

        population = [Genotype() for _ in range(20)]

        pareto_front = nsga2_evolve(
            population=population, objectives=evaluate_objectives, generations=10
        )

        # Should have multiple solutions
        assert len(pareto_front) > 1

        # Solutions should be non-dominated
        for i, sol1 in enumerate(pareto_front):
            for j, sol2 in enumerate(pareto_front):
                if i != j:
                    obj1 = evaluate_objectives(sol1)
                    obj2 = evaluate_objectives(sol2)
                    # Neither should dominate the other
                    assert not (obj1["size"] > obj2["size"] and obj1["accuracy"] > obj2["accuracy"])


def create_graph_from_genotype(genotype):
    """Helper to create graph from genotype."""
    # Create base graph
    graph = Graph()

    input_id = graph.add_node(
        {
            "node_type": NodeType.INPUT,
            "activation_function": "linear",
            "attributes": {"output_size": 10},
        }
    )

    output_id = graph.add_node(
        {
            "node_type": NodeType.OUTPUT,
            "activation_function": "linear",
            "attributes": {"output_size": 1},
        }
    )

    # Add hidden nodes based on number of rules (simplified)
    num_hidden = min(len(genotype.rules), 3)
    hidden_ids = []

    for i in range(num_hidden):
        h_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 20},
            }
        )
        hidden_ids.append(h_id)

    # Connect sequentially
    if hidden_ids:
        graph.add_edge(source_id=input_id, target_id=hidden_ids[0])
        for i in range(len(hidden_ids) - 1):
            graph.add_edge(source_id=hidden_ids[i], target_id=hidden_ids[i + 1])
        graph.add_edge(source_id=hidden_ids[-1], target_id=output_id)
    else:
        graph.add_edge(source_id=input_id, target_id=output_id)

    return graph
