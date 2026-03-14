import octagon

octagon1 = octagon.Octagon(side=8)
print("Описанная окружность:", octagon1.RadiusAndAreaOfCircumscribedCircle())
print("Вписанная окружность: ", octagon1.RadiusAndAreaOfAnInscribedCircle())
print("Периметр и площадь:   ", octagon1.PerimetrAndArea())
octagon1.draw()