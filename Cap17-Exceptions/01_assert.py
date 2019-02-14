#!/usr/bin/env python3


# assertion

def KelvinToFahreinheit(Temperatura):
    assert (Temperatura >= 0), 'Colder than absolute zero'
    return ((Temperatura - 273)*1.8) + 32

print(KelvinToFahreinheit(273))
print(KelvinToFahreinheit(-1))