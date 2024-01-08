import unittest
from Ant_hill import Ant_hill







class TestAntHill(unittest.TestCase):
    def test_init(self):
        r1_f50 = Ant_hill()

        #test init self.food
        self.assertEqual(r1_f50.food, 0, "test init food")

        # test init self.day
        self.assertEqual(r1_f50.day, 0, "test init day")

        # test init self.ant_list
        self.assertEqual(r1_f50.ant_list, [], "test init ant_list")


        #self.assertIsInstance(r1_F50, Basic_ant)

    def test_hill_constructor(self):
        # Vérifie si hill_constructor ajoute correctement des reines et des fourmis à ant_list
        r1_f50 = Ant_hill()
        r1_f50.hill_constructor(1, 50, 0)
        r2_f50 = Ant_hill()
        r2_f50.hill_constructor(2, 50, 2)
        r0_f50 = Ant_hill()
        r0_f50.hill_constructor(0, 50, 0)
        r1_f0 = Ant_hill()
        r1_f0.hill_constructor(1, 0, 0)
        r0_f0 = Ant_hill()
        r0_f0.hill_constructor(0, 0, 0)

        self.assertEqual(len(r1_f50.ant_list), 51, "test nbr tot de fourmis")
        self.assertEqual(len(r2_f50.ant_list), 52, "test nbr tot de fourmis")
        self.assertEqual(len(r0_f50.ant_list), 50, "test nbr tot de fourmis")
        self.assertEqual(len(r1_f0.ant_list), 1, "test nbr tot de fourmis")
        self.assertEqual(len(r0_f0.ant_list), 0, "test nbr tot de fourmis")


        self.assertEqual(sum('Reine' in str(item) for item in r1_f50.ant_list), 1, "test nbr de Reine")
        self.assertEqual(sum('Reine' in str(item) for item in r2_f50.ant_list), 2, "test nbr de Reine")
        self.assertEqual(sum('Reine' in str(item) for item in r0_f50.ant_list), 0, "test nbr de Reine")
        self.assertEqual(sum('Reine' in str(item) for item in r1_f0.ant_list), 1, "test nbr de Reine")
        self.assertEqual(sum('Reine' in str(item) for item in r0_f0.ant_list), 0, "test nbr de Reine")


        self.assertEqual(sum('Fourmis basique' in str(item) for item in r1_f50.ant_list), 50, "test nbr de Fourmi")
        self.assertEqual(sum('Fourmis basique' in str(item) for item in r2_f50.ant_list), 50, "test nbr de Fourmi")
        self.assertEqual(sum('Fourmis basique' in str(item) for item in r0_f50.ant_list), 50, "test nbr de Fourmi")
        self.assertEqual(sum('Fourmis basique' in str(item) for item in r1_f0.ant_list), 0, "test nbr de Fourmi")
        self.assertEqual(sum('Fourmis basique' in str(item) for item in r0_f0.ant_list), 0, "test nbr de Fourmi")


        self.assertEqual(r1_f50.ant_list[1].birth, 0, "test le jour de naissance de la fourmis")
        self.assertEqual(r2_f50.ant_list[1].birth, 2, "test le jour de naissance de la fourmis")
        self.assertEqual(r1_f50.ant_list[0].birth, 0, "test le jour de naissance de la Reine")
        self.assertEqual(r2_f50.ant_list[0].birth, 2, "test le jour de naissance de la Reine")

    def test_nbr_ant_alive(self):
        r1_f50 = Ant_hill()
        r1_f50.hill_constructor(1, 50, 0)

        r2_f50 = Ant_hill()
        r2_f50.hill_constructor(2, 50, 2)
        r2_f50.killAnt()

        r0_f50 = Ant_hill()
        r0_f50.hill_constructor(0, 50, 0)
        r0_f50.addAnt(1)

        r1_f0 = Ant_hill()
        r1_f0.hill_constructor(1, 0, 0)

        r0_f0 = Ant_hill()
        r0_f0.hill_constructor(0, 0, 0)

        self.assertEqual(r1_f50.nbr_ant_alive(), 51, "test nbr de fourmis vivante")
        self.assertEqual(r1_f0.nbr_ant_alive(), 1, "test nbr de fourmis vivante")
        self.assertEqual(r0_f0.nbr_ant_alive(), 0, "test nbr de fourmis vivante")
        self.assertEqual(r2_f50.nbr_ant_alive(), 51, "test nbr de fourmis vivante apres en avoir tuer 1")
        self.assertEqual(r0_f50.nbr_ant_alive(), 51, "test nbr de fourmis vivante apres en avoir ajouter 1")

    def test_addAnt(self):
        r1_f50 = Ant_hill()
        r1_f50.hill_constructor(1, 50, 0)
        r1_f50.addAnt(1)

        r2_f50 = Ant_hill()
        r2_f50.hill_constructor(2, 50, 2)
        for x in range(123):
            r2_f50.addAnt(1)

        r1_f0 = Ant_hill()
        r1_f0.hill_constructor(1, 0, 0)
        r1_f0.addAnt(1)

        self.assertEqual(sum('Fourmis basique' in str(item) for item in r1_f50.ant_list), 51, "test ajout d'une fourmis basique")
        self.assertEqual(sum('Fourmis basique' in str(item) for item in r2_f50.ant_list), 173, "test ajout 123 fourmis basique")
        self.assertEqual(sum('Fourmis basique' in str(item) for item in r1_f0.ant_list), 1, "test ajout d'une fourmis basique la ou il n'y a pas de fourmis basique")

    def test_addQueen(self):
        r1_f50 = Ant_hill()
        r1_f50.hill_constructor(1, 50, 0)
        r1_f50.addQueen(1)

        r2_f50 = Ant_hill()
        r2_f50.hill_constructor(2, 50, 2)
        for x in range(123):
            r2_f50.addQueen(1)

        r0_f50 = Ant_hill()
        r0_f50.hill_constructor(0, 50, 2)
        r0_f50.addQueen(1)

        self.assertEqual(sum('Reine' in str(item) for item in r1_f50.ant_list), 2, "test ajout d'une Reine")
        self.assertEqual(sum('Reine' in str(item) for item in r2_f50.ant_list), 125, "test ajout 123 Reines")
        self.assertEqual(sum('Reine' in str(item) for item in r0_f50.ant_list), 1, "test ajout d'une Reine dans un fourmilière ou il'y en a pas ")

    def test_killAnt(self):
        r1_f50 = Ant_hill()
        r1_f50.hill_constructor(1, 50, 0)
        r1_f50.killAnt()

        r2_f2000 = Ant_hill()
        r2_f2000.hill_constructor(2, 2000, 2)
        for x in range(250):
            r2_f2000.killAnt()

        r0_f0 = Ant_hill()
        r0_f0.hill_constructor(0, 0, 0)


        self.assertEqual(len(r1_f50.ant_list), 50, "test ajout d'une fourmis basique")
        self.assertEqual(len(r2_f2000.ant_list), 1752, "test ajout 123 fourmis basique")

        with self.assertRaises(IndexError):
            r0_f0.killAnt()








if __name__ == '__main__':
    unittest.main()