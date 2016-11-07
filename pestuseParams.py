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
NOMBRE_PERIODES = 10
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
      u"Combien de produits différents pouvez-vous produire ?", 
      [u"1", u"2"], 
      [u"2"], 
      u"Vous pouvez produire deux produits différents : le produit Y et le produit Z"
      ], 
      [
      u"A partir du moment où vous aurez choisi la quantité de matière X pour produire le produit Y, vous savez exactement la quantité de produit Y que vous allez obtenir.", 
      [u"Vrai", u"Faux"], 
      [u"Vrai"], 
      u"La quantité de produit Y obtenue ne dépend que de la quantité de matière première X choisie."
      ],
      [
      u"A partir du moment où vous aurez choisi la quantité de matière X pour produire le produit Z, vous savez exactement la quantité de produit Z que vous allez obtenir.", 
      [u"Vrai", u"Faux"], 
      [u"Faux"], 
      u"La quantité de produit Y obtenue ne dépend que de la quantité de matière première X choisie."
      ],
      [
      u"Combien d’ateliers sont utilisés pour la production de chacun des produits ?", 
      [u"5 ateliers pour\n   le produit Y et\n5 ateliers pour\n   le produit Z", u"10 ateliers pour\n   le produit Y et\n0 atelier pour\n   le produit Z", u"3 ateliers pour\n   le produit Y et\n7 ateliers pour\n   le produit Z"], 
      [u"5 ateliers pour\n   le produit Y et\n5 ateliers pour\n   le produit Z"], 
      u"Il y a 5 ateliers pour le produit Y et 5 ateliers pour le produit Z"
      ],
      [
      u"La matière première X vous permet d’avoir plus de produit Y et de produit Z. Vous avez intérêt à utiliser une quantité maximum de matière première X.", 
      [u"Oui", u"Non"], 
      [u"Non"], 
      u"Plus vous mettez de matière première X, plus vous obtenez une quantité élevée de produit Y et de produit Z. Cependant, la matière première X est coûteuse. Vous devez bien choisir la quantité de matière première que vous souhaitez utiliser car elle vous rapporte mais elle vous coûte également."
      ],
      [
      u"La matière première X coûte 1 ECU par unité tandis que les produits (Y ou Z) ont un prix de 10 ECUs par unité.", 
      [u"Vrai", u"Faux"], 
      [u"Vrai"], 
      u"Toute unité de matière première utilisée vous coutera 1 ECU. Toute unité de produit (Y ou Z) vous sera rachetée 10 ECUs."
      ],
      [
      u"Vous êtes obligés de produire une quantité positive de produit Y et une quantité positive de produit Z.", 
      [u"Vrai", u"Faux"], 
      [u"Faux"], 
      u"Vous pouvez choisir de ne pas produire le produit Y et/ou de ne pas produire le produit Z. Il vous suffit simplement de choisir une quantité nulle de matière première X."
      ],       
      ]
QCWEX = [
      [
      u"Il y a 5 ateliers pour la production du produit Y et 5 ateliers pour la production du produit Z.", 
      [u"Vrai", u"Faux"], 
      [u"Faux"], 
      u"La quantité de produit Z obtenue ne dépend pas uniquement de la quantité de matière première X choisie. Elle dépend également du résultat du tirage d’un dé."
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
      u"L’assurance sur la production du produit Y ne vous verse une indemnité que si le dé tombe sur le chiffre 1", 
      [u"Vrai", u"Faux"], 
      [u"Vrai"], 
      u"Vous payez la prime d’assurance quel que soit le résultat du tirage de dé. Mais, si le rendement du produit Y est minimal (si le dé tombe sur le chiffre 1), vous recevez une indemnité. Si le dé tombe sur un chiffre autre que le 1, vous ne touchez pas l’indemnité."
      ], 
      ]
QCWEI = [
      [
      u"Il y a 5 ateliers pour la production du produit Y et 5 ateliers pour la production du produit Z.", 
      [u"Vrai", u"Faux"], 
      [u"Faux"], 
      u"C’est vous qui choisissez le nombre d’ateliers que vous souhaitez affecter à la production du produit Z, le reste des ateliers seront affectés à la production du produit Y."
      ], 
      [
      u"L’assurance sur la production du produit Y ne vous verse une indemnité que si le dé tombe sur le chiffre 1.", 
      [u"Vrai", u"Faux"], 
      [u"Vrai"], 
      u"Vous payez la prime d’assurance quel que soit le résultat du tirage de dé. Mais, si le rendement du produit Y est minimal (si le dé tombe sur le chiffre 1), vous recevez une indemnité. Si le dé tombe sur un chiffre autre que le 1, vous ne touchez pas l’indemnité."
      ], 
      ]      
QCWIE = [
      [
      u"Il y a 5 ateliers pour la production du produit Y et 5 ateliers pour la production du produit Z.", 
      [u"Vrai", u"Faux"], 
      [u"Faux"], 
      u"C’est vous qui choisissez le nombre d’ateliers que vous souhaitez affecter à la production du produit Z, le reste des ateliers seront affectés à la production du produit Y."
      ], 
      [
      u"L’assurance sur la production du produit Y ne vous verse une indemnité que si le dé tombe sur le chiffre 1.", 
      [u"Vrai", u"Faux"], 
      [u"Vrai"], 
      u"Vous payez la prime d’assurance quel que soit le résultat du tirage de dé. Mais, si le rendement du produit Y est minimal (si le dé tombe sur le chiffre 1), vous recevez une indemnité. Si le dé tombe sur un chiffre autre que le 1, vous ne touchez pas l’indemnité."
      ], 
      ]  
