class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        out = f"Rectangle(width={self.width}, height={self.height})"
        return out

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        # Draws the shape with "*"s.
        if self.height > 50 or self.width > 50:
            out = "Too big for picture."
        else:
            out = ""
            for _ in range(self.height):
                out += f"{'*' * self.width}\n"
        return out

    def get_amount_inside(self, other_rect):
        # This function calculates how many rectangles(rect2) can be fitted into another one(rect1).
        # rect1.get_amount_inside(rect2)
        return (self.width // other_rect.width) * (self.height // other_rect.height)


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(width=side, height=side)
        self.side = side

    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side

    def set_width(self, width):
        self.side = width
        self.height = width
        self.width = width

    def set_height(self, height):
        self.side = height
        self.height = height
        self.width = height

    def __str__(self):
        out = f"Square(side={self.side})"
        return out


if __name__ == '__main__':
    rect = Rectangle(5, 10)
    print(rect.get_area())
    rect.set_width(3)
    print(rect.get_perimeter())
    print(rect)

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)

    print(rect.get_picture())
    print(rect.get_amount_inside(sq))
