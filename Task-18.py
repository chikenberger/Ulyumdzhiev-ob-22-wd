class GeometricFigure:
    def __init__(self, square, perimeter):
        self.square = square
        self.perimeter = perimeter

    def getFigureInfo(self):
        print(f'площадь - {self.square}, периметр - {self.perimeter}')

rect = GeometricFigure(10, 14)
rect.getFigureInfo()
