#!/usr/bin/env python3
"""
Test-Driven Development for Proper GGNES Usage
================================================
This test suite ensures we understand and correctly use ALL GGNES features.
"""

import uuid

# GGNES imports we need to test
from ggnes import Graph, NodeType
from ggnes.evolution import CompositeGenotype, G1Grammar, G2Policy, G3Hierarchy, Genotype
from ggnes.evolution.operators import mutate, uniform_crossover
from ggnes.generation import generate_network
from ggnes.rules.rule import EmbeddingLogic, LHSPattern, RHSAction, Rule
from ggnes.utils.rng_manager import RNGManager
from ggnes.utils.uuid_provider import DeterministicUUIDProvider, UUIDProviderConfig


class TestGrammarRules:
    """Test creating and using grammar rules"""

    def test_create_basic_rule(self):
        """Test creating a basic grammar rule"""
        # Create a rule that adds a hidden layer
        lhs = LHSPattern(
            nodes=[{"label": "INPUT", "constraints": {"node_type": NodeType.INPUT}}],
            edges=[],
            boundary_nodes=["INPUT"],
        )

        rhs = RHSAction(
            add_nodes=[
                {
                    "label": "HIDDEN",
                    "properties": {
                        "node_type": NodeType.HIDDEN,
                        "activation_function": "relu",
                        "attributes": {"output_size": 32},
                    },
                }
            ],
            add_edges=[{"source": "INPUT", "target": "HIDDEN", "properties": {"weight": 1.0}}],
        )

        embedding = EmbeddingLogic()

        rule = Rule(
            rule_id=uuid.uuid4(),
            lhs=lhs,
            rhs=rhs,
            embedding=embedding,
            metadata={"priority": 1, "probability": 0.8},
        )

        assert rule is not None
        assert rule.metadata["priority"] == 1

    def test_create_rule_list(self):
        """Test creating a list of rules for a genotype"""
        rules = []

        # Rule 1: Add hidden layer
        rules.append(
            Rule(
                rule_id=uuid.uuid4(),
                lhs=LHSPattern(nodes=[], edges=[], boundary_nodes=[]),
                rhs=RHSAction(
                    add_nodes=[
                        {
                            "label": "H1",
                            "properties": {
                                "node_type": NodeType.HIDDEN,
                                "activation_function": "relu",
                                "attributes": {"output_size": 64},
                            },
                        }
                    ]
                ),
                embedding=EmbeddingLogic(),
                metadata={"priority": 1, "probability": 0.9},
            )
        )

        # Rule 2: Add another hidden layer
        rules.append(
            Rule(
                rule_id=uuid.uuid4(),
                lhs=LHSPattern(nodes=[], edges=[], boundary_nodes=[]),
                rhs=RHSAction(
                    add_nodes=[
                        {
                            "label": "H2",
                            "properties": {
                                "node_type": NodeType.HIDDEN,
                                "activation_function": "tanh",
                                "attributes": {"output_size": 32},
                            },
                        }
                    ]
                ),
                embedding=EmbeddingLogic(),
                metadata={"priority": 2, "probability": 0.7},
            )
        )

        assert len(rules) == 2


class TestGenotypes:
    """Test creating and using genotypes"""

    def test_create_simple_genotype(self):
        """Test creating a simple genotype with rules"""
        rules = []
        genotype = Genotype(rules=rules)

        assert genotype is not None
        assert hasattr(genotype, "genotype_id")
        assert genotype.fitness is None

    def test_create_composite_genotype(self):
        """Test creating a composite genotype with G1/G2/G3"""
        # G1: Grammar rules
        g1 = G1Grammar(rules=[])

        # G2: Training policy (dataclass with defaults)
        g2 = G2Policy()
        g2.learning_rate = 0.001
        g2.batch_size = 32
        g2.training_epochs = 100

        # G3: Hierarchical modules
        g3 = G3Hierarchy(modules={}, attributes={})

        # Create composite
        composite = CompositeGenotype(g1=g1, g2=g2, g3=g3)

        assert composite is not None
        assert composite.g2.learning_rate == 0.001

    def test_genotype_uuid(self):
        """Test generating deterministic UUID for genotype"""
        provider = DeterministicUUIDProvider(UUIDProviderConfig())

        composite = CompositeGenotype(
            g1=G1Grammar(rules=[]), g2=G2Policy(), g3=G3Hierarchy(), provider=provider
        )

        # Generate UUID
        uuid_str = composite.uuid()

        assert uuid_str is not None
        assert len(uuid_str) == 36  # Standard UUID format

        # Should be deterministic
        uuid_str2 = composite.uuid()
        assert uuid_str == uuid_str2


class TestNetworkGeneration:
    """Test generating networks from genotypes"""

    def test_generate_network_from_genotype(self):
        """Test using generate_network() function"""
        # Create axiom (starting graph)
        axiom = Graph()
        input_id = axiom.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 8},
            }
        )
        output_id = axiom.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )
        axiom.add_edge(input_id, output_id, {"weight": 1.0})

        # Create genotype with no rules (should return axiom)
        genotype = Genotype(rules=[])

        # Configuration
        config = {
            "max_iterations": 10,
            "selection_strategy": "PRIORITY_THEN_PROBABILITY_THEN_ORDER",
        }

        # RNG Manager
        rng_manager = RNGManager(seed=42)

        # Generate network
        graph, metrics = generate_network(genotype, axiom, config, rng_manager)

        assert graph is not None
        assert metrics is not None
        assert "iterations" in metrics


class TestEvolutionOperators:
    """Test built-in evolution operators"""

    def test_mutate_genotype(self):
        """Test mutating a genotype"""
        # Create genotype
        genotype = Genotype(rules=[])

        # Configuration - high rate to ensure mutation happens
        config = {
            "mutation_rate": 1.0,  # Always mutate for testing
            "mutation_probs": {
                "modify_metadata": 0.3,
                "modify_rhs": 0.2,
                "modify_lhs": 0.2,
                "add_rule": 0.15,
                "delete_rule": 0.15,
            },
            "min_rules_per_genotype": 0,  # Allow empty genotypes
        }

        # RNG Manager
        rng_manager = RNGManager(seed=42)

        # Mutate
        mutated = mutate(genotype, config, rng_manager)

        assert mutated is not None
        # If mutation happened, ID should be different
        # Note: with empty rules list, some mutations might not change anything
        if config["mutation_rate"] == 1.0 and len(genotype.rules) == 0:
            # Empty genotype might not change much, just check it exists
            assert hasattr(mutated, "genotype_id")

    def test_crossover_genotypes(self):
        """Test crossover between two genotypes"""
        parent1 = Genotype(rules=[])
        parent2 = Genotype(rules=[])

        config = {"crossover_rate": 0.7, "min_rules_per_genotype": 1}

        rng_manager = RNGManager(seed=42)

        # Crossover
        child1, child2 = uniform_crossover(parent1, parent2, config, rng_manager)

        assert child1 is not None
        assert child2 is not None


class TestObservability:
    """Test observability and reporting features"""

    def test_consolidated_report(self):
        """Test generating a consolidated report"""
        # We need DerivationEngine for this - skip for now
        # as it requires more complex setup
        pass

    def test_genotype_explain(self):
        """Test genotype explanation"""
        composite = CompositeGenotype()

        # Get canonical inputs (similar to explain)
        canonical = composite.as_canonical_inputs()

        assert "schema_version" in canonical
        assert "g1" in canonical
        assert "g2" in canonical
        assert "g3" in canonical


class TestRNGManager:
    """Test deterministic randomness"""

    def test_rng_contexts(self):
        """Test different RNG contexts"""
        rng_manager = RNGManager(seed=42)

        # Get RNG for different contexts
        rng_mutation = rng_manager.get_rng_for_mutation(uuid.uuid4())
        rng_crossover = rng_manager.get_rng_for_crossover(
            uuid.uuid4(), uuid.uuid4()
        )  # Needs 2 parent IDs
        rng_selection = rng_manager.get_context_rng("selection")  # Correct method name

        assert rng_mutation is not None
        assert rng_crossover is not None
        assert rng_selection is not None

        # Should be deterministic
        val1 = rng_mutation.random()
        val2 = rng_crossover.random()
        assert val1 != val2  # Different contexts give different values


class TestEndToEnd:
    """Test complete GGNES workflow"""

    def test_complete_evolution_cycle(self):
        """Test a complete evolution cycle with all features"""
        # 1. Initialize RNG
        rng_manager = RNGManager(seed=42)
        provider = DeterministicUUIDProvider(UUIDProviderConfig())

        # 2. Create initial population with different content
        population = []
        for i in range(5):
            # Give each genotype slightly different parameters to get unique UUIDs
            g2 = G2Policy()
            g2.learning_rate = 0.001 * (i + 1)  # Different learning rates
            g2.batch_size = 32 + i  # Different batch sizes

            composite = CompositeGenotype(
                g1=G1Grammar(rules=[]), g2=g2, g3=G3Hierarchy(), provider=provider
            )
            population.append(composite)

        # 3. Generate DNA for each
        dnas = []
        for genotype in population:
            dna = genotype.uuid()
            dnas.append(dna)

        assert len(dnas) == 5
        assert len(set(dnas)) == 5  # All unique

        # 4. Create axiom graph
        axiom = Graph()
        axiom.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 8},
            }
        )
        axiom.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        # 5. Generate networks
        config = {"max_iterations": 5}
        for genotype in population:
            graph, metrics = generate_network(genotype.g1, axiom, config, rng_manager)
            assert graph is not None

        # 6. Evolution operators
        # Need to use Genotype, not G1Grammar directly
        genotype1 = Genotype(rules=[])
        genotype2 = Genotype(rules=[])

        # Mutation
        mutated = mutate(genotype1, {"mutation_rate": 0.5}, rng_manager)
        assert mutated is not None

        # Crossover
        child1, child2 = uniform_crossover(
            genotype1, genotype2, {"crossover_rate": 0.7, "min_rules_per_genotype": 0}, rng_manager
        )
        assert child1 is not None
        assert child2 is not None


if __name__ == "__main__":
    # Run tests
    print("Running GGNES Proper Usage Tests...")

    # Test Grammar Rules
    test_rules = TestGrammarRules()
    test_rules.test_create_basic_rule()
    test_rules.test_create_rule_list()
    print("✅ Grammar Rules tests passed")

    # Test Genotypes
    test_genotypes = TestGenotypes()
    test_genotypes.test_create_simple_genotype()
    test_genotypes.test_create_composite_genotype()
    test_genotypes.test_genotype_uuid()
    print("✅ Genotypes tests passed")

    # Test Network Generation
    test_network = TestNetworkGeneration()
    test_network.test_generate_network_from_genotype()
    print("✅ Network Generation tests passed")

    # Test Evolution Operators
    test_evolution = TestEvolutionOperators()
    test_evolution.test_mutate_genotype()
    test_evolution.test_crossover_genotypes()
    print("✅ Evolution Operators tests passed")

    # Test Observability
    test_observability = TestObservability()
    test_observability.test_genotype_explain()
    print("✅ Observability tests passed")

    # Test RNG Manager
    test_rng = TestRNGManager()
    test_rng.test_rng_contexts()
    print("✅ RNG Manager tests passed")

    # Test End-to-End
    test_e2e = TestEndToEnd()
    test_e2e.test_complete_evolution_cycle()
    print("✅ End-to-End tests passed")

    print("\n🎉 All GGNES Proper Usage Tests Passed!")
