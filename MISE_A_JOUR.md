# Procédure de mise à jour quotidienne

Site : fiches neutres sur les candidats à la présidentielle 2027 (1er tour 18 avril 2027, 2nd tour 2 mai 2027).
Dépôt : github.com/ltbrokerolivier-a11y/presidentielle-2027 (public), publié par GitHub Pages depuis la racine de `main`.
La page `index.html` lit `data/candidats.json` : une mise à jour quotidienne consiste uniquement à modifier ce fichier.

## Chaque jour
1. Rechercher les nouvelles des dernières 24-48 h : nouvelles candidatures, retraits, ralliements, programmes publiés, propositions annoncées, interviews vidéo, décisions du Conseil constitutionnel (parrainages, liste officielle le 26 mars 2027), résultats officiels.
2. Pour CHAQUE candidat qui a une actualité, et en tournant chaque jour sur 4 à 5 candidats à fiche courte, compléter : fonction, parcours, propositions (thème + texte + source), liens officiels vérifiés, vidéos.
3. Ajouter une ligne datée dans `actualites` pour chaque fait marquant (garder les 40 plus récentes).
4. Mettre `meta.derniere_mise_a_jour` à la date du jour. Lire le fichier actuel du dépôt (get_file_contents), le modifier, vérifier localement que le JSON est valide et que `python3 scripts/build.py` affiche OK, puis l'envoyer sur `main` (push_files). Ne jamais modifier `index.html` sauf correction nécessaire.

## Règles de neutralité (obligatoires)
- Même structure de fiche pour tous ; ordre alphabétique ; aucun sondage, pronostic, qualificatif ou avis.
- Propositions reformulées de façon factuelle, sans adjectif évaluatif, chacune avec une source https (média reconnu, site officiel du candidat, document officiel). Pas de sites de contenu généré (ex. elyseescope) ni de forums.
- Aucune citation de plus de 15 mots ; reformuler.
- Équilibre : chercher séparément pour chaque candidat ; ne pas enrichir un camp seulement.
- Pas de photos de personnes (initiales uniquement).
- Vidéos : seulement des vidéos réelles dont l'identifiant YouTube a été vérifié (champ `videos: [{"titre","date","youtube":"ID"}]`) ; de préférence chaînes officielles des candidats ou médias (débats, journaux télévisés, interviews).
- Ne jamais inventer un lien, un chiffre ou une date.

## Règles légales de période électorale (obligatoires)
- Week-ends de vote : du samedi 17 avril 2027 à 0 h au dimanche 18 avril 20 h, et du samedi 1er mai 2027 à 0 h au dimanche 2 mai 20 h (dès le vendredi minuit pour l'outre-mer qui vote le samedi) : NE RIEN AJOUTER qui ressemble à de la propagande (déclarations, propositions, vidéos, citations de meeting). Seules les informations pratiques (horaires, procuration) sont autorisées.
- Jamais de sondage, ni sa mention ou son commentaire, et en particulier du vendredi minuit au dimanche 20 h des week-ends de vote.
- Aucun résultat partiel ou estimation avant 20 h 00 le dimanche du vote ; ensuite seulement les résultats officiels (ministère de l'Intérieur, puis Conseil constitutionnel), en citant la source.
- Sources autorisées pour le journal : sources officielles (Conseil constitutionnel, ministère de l'Intérieur, service-public, vie-publique, Légifrance, sites officiels des candidats) et médias reconnus (AFP, Le Monde, Le Figaro, Libération, franceinfo, LCP, Public Sénat, Ouest-France, 20 Minutes, Les Échos, BFMTV, TF1info, Europe 1, RTL, Toute l'Europe, etc.). Pas de contenus générés par IA, de forums ni de vidéos non vérifiées.
- Affaires judiciaires : uniquement des faits établis par une source fiable, au conditionnel pour ce qui est en cours, en rappelant la présomption d'innocence.

## Fin de campagne
- Le 26 mars 2027 : passer les candidats non retenus dans `retires`.
- Le 18 avril et le 2 mai 2027 : ajouter les résultats officiels (ministère de l'Intérieur / Conseil constitutionnel) dans `actualites`.
- Après la proclamation des résultats du 2nd tour : dernière mise à jour, puis arrêt.
