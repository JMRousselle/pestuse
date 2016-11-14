# -*- coding: utf-8 -*-
"""
Ce module contient les variables et les paramètres de la partie
Les variables ne doivent pas être changées
Les paramètres peuvent être changés, mais, par sécurité, demander au développeur
"""

# variables
BASELINE = 0

# paramètres
TREATMENT = BASELINE
TAUX_CONVERSION = 0.0005
NOMBRE_PERIODES = 6
TAILLE_GROUPES = 0
GROUPES_CHAQUE_PERIODE = False
MONNAIE = u"ecu"

# DECISION
DECISION_MIN = 0
DECISION_MAX = 100
DECISION_STEP = 1

# Parametres des curseurs
MIN_X_POUR_Y = 0
MAX_X_POUR_Y = 600
MIN_X_POUR_Z = 0
MAX_X_POUR_Z = 600

PRIX_PRODUIT_Y = 10
PRIX_PRODUIT_Z = 10
PRIX_PRODUIT_X = 1

BONUS = 1500
MONTANT_FIXE = 300
ASSUR = 12
INDEMNITE = 48

BETA = -0.1


# TEXTE DU QUESTIONNAIRE DE COMPREHENSION Question, Choix, Bonnes reponse puis texte de réponse
QCBEN = [
      [
      u"Quel nombre maximal de produits différents pouvez-vous produire ?", 
      [u"1", u"2"], 
      [u"2"], 
      u"Vous pouvez produire deux produits différents : le produit Y et le produit Z"
      ], 
      [
      u"A partir du moment où vous aurez choisi la quantité d'intrant X pour produire le produit Y, vous savez exactement la quantité de produit Y que vous allez obtenir.", 
      [u"Vrai", u"Faux"], 
      [u"Vrai"], 
      u"La quantité de produit Y obtenue ne dépend que de la quantité d'intrant X choisie."
      ],
      [
      u"A partir du moment où vous aurez choisi la quantité d'intrant X pour produire le produit Z, vous savez exactement la quantité de produit Z que vous allez obtenir.", 
      [u"Vrai", u"Faux"], 
      [u"Faux"], 
      u"La quantité de produit Z obtenue ne dépend que de la quantité d'intrant X choisie."
      ],
      [
      u"Combien d’ateliers sont utilisés pour la production de chacun des produits ?", 
      [u"5 ateliers pour\n   le produit Y et\n5 ateliers pour\n   le produit Z", u"10 ateliers pour\n   le produit Y et\n0 atelier pour\n   le produit Z", u"3 ateliers pour\n   le produit Y et\n7 ateliers pour\n   le produit Z"], 
      [u"5 ateliers pour\n   le produit Y et\n5 ateliers pour\n   le produit Z"], 
      u"Il y a 5 ateliers pour le produit Y et 5 ateliers pour le produit Z"
      ],
      [
      u"L'intrant X vous permet d’avoir plus de produit Y et de produit Z. Vous avez toujours intérêt à utiliser une quantité maximum d'intrant X.", 
      [u"Oui", u"Non"], 
      [u"Non"], 
      u"Plus vous mettez d'intrant X, plus vous obtenez une quantité élevée de produit Y et de produit Z. Cependant, l'intrant X est coûteux. Vous devez bien choisir la quantité d'intrant que vous souhaitez utiliser car elle vous rapporte mais elle vous coûte également."
      ],
      [
      u"L'intrant X coûte 1 ECU par unité tandis que les produits (Y ou Z) ont un prix de 10 ECUs par unité.", 
      [u"Vrai", u"Faux"], 
      [u"Vrai"], 
      u"Toute unité d'intrant utilisée vous coutera 1 ECU. Toute unité de produit (Y ou Z) vous sera rachetée 10 ECUs."
      ],
      [
      u"Vous êtes obligés de produire une quantité positive de produit Y et une quantité positive de produit Z.", 
      [u"Vrai", u"Faux"], 
      [u"Faux"], 
      u"Vous pouvez choisir de ne pas produire le produit Y et/ou de ne pas produire le produit Z. Il vous suffit simplement de choisir une quantité nulle d'intrant X."
      ],       
      ]
QCWEX = [
      [
      u"Il y a 5 ateliers pour la production du produit Y et 5 ateliers pour la production du produit Z.", 
      [u"Vrai", u"Faux"], 
      [u"Faux"], 
      u"C’est vous qui choisissez le nombre d’ateliers que vous souhaitez affecter à la production du produit Y, le reste des ateliers seront affectés à la production du produit Z."
      ], 
      ]
QCWEA = [
      ]
QCWIN = [
      [
      u"Il y a 5 ateliers pour la production du produit Y et 5 ateliers pour la production du produit Z.", 
      [u"Vrai", u"Faux"], 
      [u"Vrai"], 
      u"C’est vrai. Cinq ateliers sont dédiés à la production du produit Y et cinq ateliers sont dédiés à la production du produit Z"
      ], 
      [
      u"L’assurance sur la production du produit Z ne vous verse une indemnité que si le dé tombe sur le chiffre 1", 
      [u"Vrai", u"Faux"], 
      [u"Vrai"], 
      u"Vous payez la prime d’assurance quel que soit le résultat du tirage de dé. Mais, si le rendement du produit Z est minimal (si le dé tombe sur le chiffre 1), vous recevez une indemnité. Si le dé tombe sur un chiffre autre que le 1, vous ne touchez pas l’indemnité."
      ], 
      ]
QCWEI = [
      [
      u"Il y a 5 ateliers pour la production du produit Y et 5 ateliers pour la production du produit Z.", 
      [u"Vrai", u"Faux"], 
      [u"Faux"], 
      u"C’est vous qui choisissez le nombre d’ateliers que vous souhaitez affecter à la production du produit Y, le reste des ateliers seront affectés à la production du produit Z."
      ], 
      [
      u"L’assurance sur la production du produit Z ne vous verse une indemnité que si le dé tombe sur le chiffre 1.", 
      [u"Vrai", u"Faux"], 
      [u"Vrai"], 
      u"Vous payez la prime d’assurance quel que soit le résultat du tirage de dé. Mais, si le rendement du produit Z est minimal (si le dé tombe sur le chiffre 1), vous recevez une indemnité. Si le dé tombe sur un chiffre autre que le 1, vous ne touchez pas l’indemnité."
      ], 
      ]      
QCWIE = [
      [
      u"Il y a 5 ateliers pour la production du produit Y et 5 ateliers pour la production du produit Z.", 
      [u"Vrai", u"Faux"], 
      [u"Faux"], 
      u"C’est vous qui choisissez le nombre d’ateliers que vous souhaitez affecter à la production du produit Y, le reste des ateliers seront affectés à la production du produit Z."
      ], 
      [
      u"L’assurance sur la production du produit Z ne vous verse une indemnité que si le dé tombe sur le chiffre 1.", 
      [u"Vrai", u"Faux"], 
      [u"Vrai"], 
      u"Vous payez la prime d’assurance quel que soit le résultat du tirage de dé. Mais, si le rendement du produit Z est minimal (si le dé tombe sur le chiffre 1), vous recevez une indemnité. Si le dé tombe sur un chiffre autre que le 1, vous ne touchez pas l’indemnité."
      ], 
      ]  
