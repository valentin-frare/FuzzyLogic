class Memberships:
    @staticmethod
    def grade(x, y, z):
        member = 0
        if x <= y:
            member = 0
        else:
            if y < x < z:
                member = (x / (z - y)) - (y / (z - y))
            else:
                if x >= z:
                    member = 1
        return member

    @staticmethod
    def grade_inverted(x, y, z):
        member = 0
        if x <= y:
            member = 1
        else:
            if y < x < z:
                member = (x / (z - y)) - (z / (z - y))
            else:
                if x >= z:
                    member = 0
        return member

    @staticmethod
    def triangle(x, a, b, c):
        member = 0;
        if x <= a:
            member = 0;
        else:
            if a < x <= b:
                member = (x / (b - a)) - (a / (b - a))
            else:
                if b < x <= c:
                    member = - (x / (c - b)) + (c / (c - b))
                else:
                    if x > c:
                        member = 0
        return member

    @staticmethod
    def trapezoid(x, a, b, c, d):
        member = 0;
        if x <= a:
            member = 0
        else:
            if a < x <= b:
                member = ( x / (b - a)) - (a / (b - a))
            else:
                if b < x <= c:
                    member = 1
                else:
                    if c < x <= d:
                        member = - (x / (d - c)) + (d / (d - c))
                    else:
                        if x > d:
                            member = 0;
        return member