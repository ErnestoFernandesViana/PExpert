class Team:
    instances_created = []
    number_of_teams = 0
    number_of_games_by_each_team = 0
    team_names = []
    team_wins = []

    def __init__(self, name, wins):
        self.name = name 
        self.wins = wins 
        Team.instances_created.append(self)

    @classmethod
    def ask_number_of_teams(cls):
        while True:
            x = int(input('Enter the number of teams in the tournament:'))
            if x < 2: 
                print('The minimum number of teams is 2, try again.')
                continue
            elif x%2 == 1:
                print('Number of teams has to be even. Try again')
            else:
                cls.number_of_teams = x
                break 
        """ cls.ask_for_team_names() """

    @staticmethod
    def check_for_valid_name(name):
        if ' ' in name:
            name_words = name.split(' ')
            if len(name_words) > 2:
                print('Team names may have at most 2 words, try again.')
                return False 
            else:
                return True 
        elif len(name) < 2:
            print('Team names may have at least 2 characters, try again.')
            return False 
        else:
            return True 

    @classmethod
    def ask_for_team_names(cls):
        for x in range(cls.number_of_teams):
            while True:
                name = input('Enter the name for team #{}:'.format(x+1))
                if cls.check_for_valid_name(name):
                    cls.team_names.append(name)
                    break
                else:
                    continue 
        """ cls.ask_number_of_games_played() """

    @classmethod
    def ask_number_of_games_played(cls):
        min = cls.number_of_teams - 1
        while True:
            answer = int(input('Enter the number of games played by each team:'))
            if answer < min:
                print('Invalid number of games. Each team plays each \
                 other at least once in the regular season, try again.')
                continue
            else: 
                cls.number_of_games_by_each_team = answer
                break 
        """ cls.ask_number_of_wins() """

    @classmethod
    def ask_number_of_wins(cls):
        max = cls.number_of_games_by_each_team
        for x in cls.team_names:
            while True:
                answer = int(input('Enter the number of wins Team {} had:'.format(x)))
                if answer > max:
                    print('The maximum number of wins is {}, try again.'.format(max))
                    continue
                elif answer < 0:
                    print('The minimum number of wins is 0, try again.')
                    continue
                else:
                    cls.team_wins.append(answer)
                    break
        """ cls.create_instances() """ 

    @classmethod
    def create_instances(cls):
        argument_tuples = list(zip(cls.team_names, cls.team_wins))
        for x in argument_tuples:
            Team(*x)
        print('Generating the games to be played in the first round of the tournament...')

    @classmethod
    def sort_by_win(cls):
        sorted_inst_list = sorted(cls.instances_created, key=lambda x: x.wins, reverse=True)
        cls.instances_created = sorted_inst_list

    @classmethod
    def printer(cls):
        instances = cls.instances_created
        for i in range(int(len(instances)/2)):
            print("Home: {} VS Away: {}".format(instances[i].name, instances[-i-1].name))

    @classmethod
    def workflow(cls):
        cls.ask_number_of_teams()
        cls.ask_for_team_names()
        cls.ask_number_of_games_played()
        cls.ask_number_of_wins()
        cls.create_instances()
        cls.sort_by_win()
        cls.printer()


if __name__ == '__main__':

    Team.workflow()
