'''
Tipos de bicicletas y componentes:

1. Bicicletas de montaña:
   - Ensamblaje: 3 horas.
   - Pintura: 1 horas.
   - Costo de producción: $120.
   - Llantas: de alto agarre.
   - Ganancia con marco de acero: $180.
   - Ganancia con marco de aluminio: $220.

2. Bicicletas de carretera:
   - Ensamblaje: 2 horas.
   - Pintura: 1 hora.
   - Costo de producción: $100.
   - Llantas: delgadas.
   - Ganancia con marco de acero: $190.
   - Ganancia con marco de aluminio: $210.

3. Bicicletas de ciudad:
   - Ensamblaje: 1 horas.
   - Pintura: 1.5 horas.
   - Costo de producción: $80.
   - Llantas: cualquiera (normal, delgada, alto agarre).
   - Ganancia con cualquier tipo de marco: $150.

 Variables:

- x1: Número de bicicletas de montaña con marco de acero producidas semanalmente.
- x2: Número de bicicletas de montaña con marco de aluminio producidas semanalmente.
- x3: Número de bicicletas de carretera con marco de acero producidas semanalmente.
- x4: Número de bicicletas de carretera con marco de aluminio producidas semanalmente.
- x5: Número de bicicletas de ciudad producidas semanalmente.

 Restricciones:

1. Restricción de ensamblaje:
   (3x1 + 3x2 + 2x3 + 2x4 + 1x5 <= 240) (horas disponibles en ensamblaje).

2. Restricción de pintura:
   (x1 + x2 + x3 + x4 + 1.5x5 <= 100) (horas disponibles en pintura).

3. Restricción de costo de materiales:
   (120x1 + 120x2 + 100x3 + 100x4 + 80x5 <= 10,000) (presupuesto máximo para materiales).

4. Restricción de llantas delgadas:
   (2x3 + 2x4 <= 150) (máximo de 120 llantas delgadas disponibles).

5. Restricción de llantas de alto agarre:
   (2x1 + 2x2 <= 80) (máximo de 80 llantas de alto agarre disponibles).

6. Restricción de llantas totales:
   (2x1 + 2x2 + 2x3 + 2x4 + 2x5 <= 300) (máximo de 100 llantas normales disponibles más los otros tipos de llantas).

7. Restricción de marcos de acero:
   (x1 + x3 <= 120) (máximo de 120 marcos de acero disponibles).

8. Restricción de marcos de aluminio:
   (x2 + x4 <= 60) (máximo de 60 marcos de aluminio disponibles).

9. Restricción de marcos totales:
   (x1 + x2 + x3 + x4 + x5 <= 180) (cantidad total de marco).

10. No se pueden producir cantidades negativas:
   (x1, x2, x3, x4, x5 >= 0).

 Función objetivo:

Maximizar la ganancia total:

Z = 180x1 + 220x2 + 190x3 + 210x4 + 150x5

 Descripción del problema actualizado:

Este problema incluye restricciones sobre la disponibilidad de tiempo de ensamblaje y pintura, el presupuesto máximo para materiales, y la disponibilidad de llantas (delgadas, normales y de alto agarre) y marcos de acero o aluminio. El objetivo es maximizar las ganancias respetando las limitaciones de tiempo, materiales y componentes. Las bicicletas de montaña y carretera con marco de acero generan mayores ganancias, mientras que las de ciudad pueden utilizar cualquier material sin afectar las ganancias.
'''

import gurobipy as gp

# Crear un nuevo modelo
m = gp.Model("bicicletas")

# Crear variables
x1 = m.addVar(vtype=gp.GRB.INTEGER, name="x1")
x2 = m.addVar(vtype=gp.GRB.INTEGER, name="x2")
x3 = m.addVar(vtype=gp.GRB.INTEGER, name="x3")
x4 = m.addVar(vtype=gp.GRB.INTEGER, name="x4")
x5 = m.addVar(vtype=gp.GRB.INTEGER, name="x5")

# Definir la función objetivo
m.setObjective(180*x1 + 220*x2 + 190*x3 + 210*x4 + 150*x5, sense=gp.GRB.MAXIMIZE)

# Agregar restricciones
m.addConstr(3*x1 + 3*x2 + 2*x3 + 2*x4 + 1*x5 <= 240)
m.addConstr(x1 + x2 + x3 + x4 + 1.5*x5 <= 100)
m.addConstr(120*x1 + 120*x2 + 100*x3 + 100*x4 + 80*x5 <= 10000)
m.addConstr(2*x3 + 2*x4 <= 150)
m.addConstr(2*x1 + 2*x2 <= 80)
m.addConstr(2*x1 + 2*x2 + 2*x3 + 2*x4 + 2*x5 <= 300)
m.addConstr(x1 + x3 <= 120)
m.addConstr(x2 + x4 <= 60)
m.addConstr(x1 + x2 + x3 + x4 + x5 <= 180)


# Optimizar el modelo
m.optimize()

# Imprimir la solución

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))

print('Objetivo: %g' % m.objVal)