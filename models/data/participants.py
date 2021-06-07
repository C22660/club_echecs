"""liste des participants au tournois"""

# enrolled = [("Durand", "Paul", "10/12/1995", "M", "2100"),
#             ("Italio", "Roberto", "15/07/1990", "M", "1200"),
#             ("Dupond", "Patrick", "01/02/1975", "M", "1600"),
#             ("Durier", "Céline", "11/01/1965", "F", "1800"),
#             ("Guillin", "Fabienne", "09/04/1982", "F", "1900"),
#             ("Dubois", "Franck", "01/09/2000", "M", "1720"),
#             ("Petit", "Romuald", "01/02/1979", "M", "1700"),
#             ("Pelletier", "Camille", "21/03/2002", "F", "1680")
#         ]

enrolled = [("Durand", "Paul", "10/12/1995", "M", "2100"),
            ("Italio", "Roberto", "15/07/1990", "M", "1200"),
            ("Dupond", "Patrick", "01/02/1975", "M", "1600"),
            ("Durier", "Céline", "11/01/1965", "F", "1800"),
            ("Guillin", "Fabienne", "09/04/1982", "F", "1900"),
            ("Dubois", "Franck", "01/09/2000", "M", "1720"),
            ("Petit", "Romuald", "01/02/1979", "M", "1700"),
        ]

# enrolled_2 = {"player_1": {name="Durand", first_name="Paul", birth="10/12/1995", sex="M", ranking="2100"),
#             (name="Italio", first_name="Roberto", birth="15/07/1990", sex="M", ranking="1200"),
#             (name="Dupond", first_name="Patrick", birth="01/02/1975", sex="M", ranking="1600"),
#             (name="Durier", first_name="Céline", birth="11/01/1965", sex="F", ranking="1800"),
#             (name="Guillin", first_name="Fabienne", birth="09/04/1982", sex="F", ranking="1900"),
#             (name="Dubois", first_name="Franck", birth="01/09/2000", sex="M", ranking="1720"),
#             (name="Petit", first_name="Romuald", birth="01/02/1979", sex="M", ranking="1700"),
#             (name="Pelletier", first_name="Camille", birth="21/03/2002", sex="F", ranking="1680")
#         ]

liste = {"id-1": "2100", "Id-2": "1200", "Id-3": "1600", "Id-4": "1800", "Id-5": "1900", "Id-6": "1720",
 "Id-7": "1700", "Id-8": "1680"
 }

liste_1 = [("id-1", "2100"), ("Id-2", "1200"), ("Id-3", "1600"), ("Id-4", "1800"), ("Id-5", "1900"),
("Id-6", "1720"), ("Id-7", "1700"), ("Id-8", "1680")
]

# une fois joué, résultat ajouté
liste_2 = [[('Id-2', '1200', '1'), ('Id-6', '1720', '0')], [('Id-3', '1600', '0.5'), ('Id-4', '1800', '0.5')],
  [('Id-8', '1680', '0'), ('Id-5', '1900', '1')], [('Id-7', '1700', '0.5'), ('id-1', '2100', '0.5')]
]
# remise au pot des joueurs sous forme d'une liste globale pour nouveau tri
liste_3 = [('Id-2', '1200', '1'), ('Id-6', '1720', '0'), ('Id-3', '1600', '0.5'), ('Id-4', '1800', '0.5'),
  ('Id-8', '1680', '0'), ('Id-5', '1900', '1'), ('Id-7', '1700', '0.5'), ('id-1', '2100', '0.5')
]