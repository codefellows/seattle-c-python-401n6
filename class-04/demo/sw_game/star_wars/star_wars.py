class ForceUser:

    def attacking(self):
        return f'{self.name} is Force attacking!'

    def getting_hit(self):
        return f'{self.name} is being attacked!'

    @classmethod
    def get_count(cls):
        return JediMaster.count + SithLord.count


class JediMaster(ForceUser):
    count = 0

    def __init__(self, name='Random Master'):
        self.name = name
        JediMaster.count += 1

    def __str__(self):
        return f'I am {self.name}'

    def __repr__(self):
        return f'JediMaster("{self.name}")'

    @staticmethod
    def get_code():
        return 'There is no emotion, there is PEACE.'

    @classmethod
    def get_count(cls):
        return cls.count


class SithLord(ForceUser):
    count = 0

    def __init__(self, name='Random Sith Lord'):
        self.name = name
        SithLord.count += 1

    @staticmethod
    def get_code():
        return 'Peace is a lie, there is only PASSION.'

    @classmethod
    def get_count(cls):
        return cls.count


if __name__ == '__main__':
    masters = []
    jedi1 = JediMaster('Yoda')
    masters.append(jedi1)
    print(jedi1.__repr__())
    # print(jedi1.attacking())
    # jedi2 = JediMaster('Mace')
    # masters.append(jedi2)
    # print(jedi2.attacking())
    # jedi3 = JediMaster()
    # masters.append(jedi3)
    # print(jedi3.attacking())
    # print(masters)
    # print(masters[0].name)
    # force_user = ForceUser()
    # force_user.name = 'Roger'
    # print(force_user.name)
