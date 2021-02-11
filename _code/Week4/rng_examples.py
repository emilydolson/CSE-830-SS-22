class MiddleSquare():
    def __init__(self, seed):
        self.seed = seed

    def get_rand(self):
        self.seed *= self.seed
        self.seed = (self.seed // 1000) % 1000000
        return self.seed

class LCG():
    def __init__(self, seed):
        self.seed = seed 
        self.a = 21
        self.c = 91
        self.m = 1000000

    def get_rand(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

def repeat_time(rng):
    seen = set()
    count = 0

    while rng.seed not in seen:
        seen.add(rng.seed)
        rng.get_rand()
        count += 1
    return count

def main():
    m_rng = MiddleSquare(3469036308563)
    print("Middle squares:")
    print(m_rng.get_rand())
    print(m_rng.get_rand())
    print(m_rng.get_rand())
    print(m_rng.get_rand())
    print("Repeat time:", repeat_time(m_rng))

    lcg_rng = LCG(2382530825308253082)
    print("LCG:")
    print(lcg_rng.get_rand())
    print(lcg_rng.get_rand())
    print(lcg_rng.get_rand())
    print(lcg_rng.get_rand())
    print("Repeat time:", repeat_time(lcg_rng))

if __name__ == "__main__":
    main()
