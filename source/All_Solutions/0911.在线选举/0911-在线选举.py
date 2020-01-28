# code block
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        person_number = max(persons)+1
        self.winner = ['' for _ in range(0,len(self.times))]
        person_record = [0 for _ in range(0,person_number)]
        max_voted = 0
        for i in range(0,len(self.times)):
            personVoted = persons[i]
            person_record[personVoted] += 1
            if person_record[personVoted] >= max_voted:
                winner_thistime = personVoted
                max_voted = person_record[personVoted]
            self.winner[i] = winner_thistime

    def q(self, t: int) -> int:
        return self.winner[bisect.bisect(self.times,t)-1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)