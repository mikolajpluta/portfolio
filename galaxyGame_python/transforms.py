def transform(self, x, y):  # useful to disable perspective viev
    #return self.transformFromperspectiveTo2D(x, y)
    return self.transform2DToPerspective(x, y)


def transformFromperspectiveTo2D(self, x, y):
    return x, y


def transform2DToPerspective(self, x, y):
    # computing y for vertical lines - temporary
    tmp_y = y / self.height * self.perspective_point_y
    if tmp_y > self.perspective_point_y:
        tmp_y = self.perspective_point_y
    # computing x
    diff_x = x - self.perspective_point_x  # point distance from perspective point x
    diff_y = self.perspective_point_y - tmp_y  # point distance from perspective point y
    factor_y = diff_y / self.perspective_point_y
    factor_y = pow(factor_y, 6)

    transformed_x = self.perspective_point_x + (diff_x * factor_y)
    transformed_y = self.perspective_point_y - (factor_y * self.perspective_point_y)
    return int(transformed_x), int(transformed_y)