import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """

    # start with overall probability = 1
    probability = 1.0

    # obtain mutation probability
    mutation = PROBS["mutation"]

    # definition for help later about transmision
    def probability_transmit(g):
        if g == 2:
            return 1 - mutation
        elif g == 1:
            return 0.5
        else:  # g == 0
            return mutation

    # loop over every person in the dataset
    for person in people:

        # determine how many genes this person has in the current assignment
        if person in two_genes:
            num_genes = 2
        elif person in one_gene:
            num_genes = 1
        else:
            num_genes = 0

        # determine whether this person is assigned the trait
        trait_bool = False
        if person in have_trait:
            trait_bool = True

        # get names of parents (if any)
        mother = people[person]["mother"]
        father = people[person]["father"]

        # if person has no parents, use unconditional gene probability
        if mother is None and father is None:
            probability_genes = PROBS["gene"][num_genes]
            
        # if person have parents, calculate probability based on parents’ transmissions
        else:
            if mother in two_genes:
                mother_gene = 2
            elif mother in one_gene:
                mother_gene = 1
            else:
                mother_gene = 0

            if father in two_genes:
                father_gene = 2
            elif father in one_gene:
                father_gene = 1
            else:
                father_gene = 0

            # probability each parent transmits the gene(call helper definition)
            probability_from_mother = probability_transmit(mother_gene)
            probability_from_father = probability_transmit(father_gene)

            # probability that child ends up with num_genes
            if num_genes == 2:
                probability_genes = probability_from_mother * probability_from_father
            elif num_genes == 1:
                probability_genes = (
                    probability_from_mother * (1 - probability_from_father)
                    + (1 - probability_from_mother) * probability_from_father
                )
            else:  # num_genes == 0
                probability_genes = (1 - probability_from_mother) * (1 - probability_from_father)

        # probability of this person showing trait given num_genes
        probability_trait = PROBS["trait"][num_genes][trait_bool]

        # multiply into the overall joint probability
        probability *= (probability_genes * probability_trait)

    # return the probability
    return probability
            

def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """

    # loop through all people
    for person in probabilities:
        if person in two_genes:
            num_genes = 2
        elif person in one_gene:
            num_genes = 1
        else:
            num_genes = 0

        # asign to trait_bool True/False
        trait_bool = (person in have_trait)

        # update data
        probabilities[person]["gene"][num_genes] += p
        probabilities[person]["trait"][trait_bool] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
