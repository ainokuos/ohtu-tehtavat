from matchers import And, All, Not, HasAtLeast, HasFewerThan, Or, PlaysIn

class QueryBuilder:
    def __init__(self, query_builder = All()):
        self.query = query_builder
    
    def build(self):
        return self.query
    
    def plays_in(self, player):
        return QueryBuilder(And(PlaysIn(player)))
    
    def has_at_leat(self, player):
        return QueryBuilder(And(HasAtLeast(player)))
    
    def has_fewer_than(self, player):
        return QueryBuilder(And(HasFewerThan(player)))
    
    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(Or(matcher1, matcher2))
    
