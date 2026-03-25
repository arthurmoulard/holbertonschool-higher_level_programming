# JavaScript DOM & API — Aide-mémoire

Un guide pratique pour sélectionner et manipuler des éléments HTML, gérer les événements et effectuer des requêtes HTTP en JavaScript vanilla.

---

## Table des matières

- [Sélectionner des éléments HTML](#-sélectionner-des-éléments-html)
- [Sélecteurs ID, classe et balise](#-sélecteurs-id-classe-et-nom-de-balise)
- [Modifier le style d'un élément](#-modifier-le-style-dun-élément)
- [Lire et modifier le contenu d'un élément](#-lire-et-modifier-le-contenu-dun-élément)
- [Modifier le DOM](#-modifier-le-dom)
- [Requêtes HTTP avec XMLHttpRequest](#-requêtes-http-avec-xmlhttprequest)
- [Requêtes HTTP avec Fetch API](#-requêtes-http-avec-fetch-api)
- [Écouter les événements DOM](#-écouter-les-événements-dom)
- [Écouter les événements utilisateur](#-écouter-les-événements-utilisateur)

---

## Sélectionner des éléments HTML

JavaScript propose plusieurs méthodes pour sélectionner des éléments dans le DOM.

```javascript
// Par ID — retourne un seul élément
const header = document.getElementById('main-header');

// Par nom de classe — retourne une HTMLCollection
const cards = document.getElementsByClassName('card');

// Par nom de balise — retourne une HTMLCollection
const paragraphs = document.getElementsByTagName('p');

// Sélecteur CSS — retourne le PREMIER résultat
const btn = document.querySelector('.btn-primary');

// Sélecteur CSS — retourne TOUS les résultats (NodeList)
const items = document.querySelectorAll('ul > li');
```

> 💡 Privilégiez `querySelector` / `querySelectorAll` — ils acceptent n'importe quel sélecteur CSS valide et sont les plus flexibles.

---

## Sélecteurs ID, classe et nom de balise

| Sélecteur | Syntaxe | Retourne | Exemple |
|-----------|---------|----------|---------|
| **ID** | `#id` | Un seul élément | `#navbar` |
| **Classe** | `.classe` | Plusieurs éléments | `.card` |
| **Balise** | `balise` | Plusieurs éléments | `div`, `p`, `a` |

```javascript
// ID — unique, retourne un seul élément
document.querySelector('#user-profile');
document.getElementById('user-profile');   // équivalent

// Classe — peut s'appliquer à plusieurs éléments
document.querySelectorAll('.highlight');
document.getElementsByClassName('highlight');  // équivalent

// Balise — sélectionne tous les éléments de ce type
document.querySelectorAll('button');
document.getElementsByTagName('button');   // équivalent

// Combinaison de sélecteurs (uniquement avec querySelector)
document.querySelector('section.active > h2');
document.querySelectorAll('input[type="text"]');
```

**Différences clés :**

- `getElementById` / `getElementsByClassName` / `getElementsByTagName` → natifs, rapides, limités
- `querySelector` / `querySelectorAll` → flexibles, supportent la syntaxe CSS complète
- `getElementsBy*` retourne une **HTMLCollection vivante** (mise à jour automatique)
- `querySelectorAll` retourne une **NodeList statique** (snapshot au moment de l'appel)

---

## Modifier le style d'un élément

```javascript
const box = document.querySelector('.box');

// Style inline — modifie une propriété directement
box.style.backgroundColor = '#3498db';
box.style.fontSize = '18px';
box.style.display = 'none';           // masquer
box.style.display = '';              // réinitialiser à la valeur CSS

// Manipuler une classe CSS (approche recommandée)
box.classList.add('active');
box.classList.remove('hidden');
box.classList.toggle('dark-mode');
box.classList.replace('ancienne-classe', 'nouvelle-classe');

// Vérifier si une classe est présente
if (box.classList.contains('active')) {
  console.log('La box est active');
}

// Lire le style calculé (après application des règles CSS)
const computed = window.getComputedStyle(box);
console.log(computed.color);         // ex. "rgb(0, 0, 0)"
```

> 💡 Utilisez `classList` plutôt que `style` — cela garde les styles dans le CSS et la logique dans le JS.

---

## Lire et modifier le contenu d'un élément

```javascript
const el = document.querySelector('#message');

// --- Lecture ---

el.textContent;   // texte brut (sûr, sans balises HTML)
el.innerHTML;     // chaîne HTML brute
el.innerText;     // texte visible uniquement (respecte la visibilité CSS)

// --- Écriture ---

// textContent — sûr, traite la valeur comme du texte brut
el.textContent = 'Bonjour, <b>monde</b>';   // affiche : Bonjour, <b>monde</b>

// innerHTML — interprète les balises HTML
el.innerHTML = 'Bonjour, <b>monde</b>';     // affiche : Bonjour, **monde**

// ⚠️ N'utilisez jamais innerHTML avec des données utilisateur — risque d'injection XSS

// --- Champs de formulaire ---
const input = document.querySelector('#username');
console.log(input.value);            // lire la valeur
input.value = 'nouvelle_valeur';     // définir la valeur
input.placeholder = 'Votre nom';     // modifier le placeholder

// --- Attributs ---
const link = document.querySelector('a');
link.getAttribute('href');           // lire
link.setAttribute('href', '/about'); // écrire
link.removeAttribute('target');      // supprimer
link.hasAttribute('disabled');       // vérifier
```

---

## Modifier le DOM

```javascript
// --- Créer des éléments ---
const div = document.createElement('div');
div.className = 'card';
div.textContent = 'Nouvelle carte';

// --- Insérer des éléments ---
const container = document.querySelector('#container');

container.appendChild(div);               // ajouter à la fin
container.prepend(div);                   // ajouter au début
container.insertBefore(div, container.firstChild); // avant un nœud de référence

// insertAdjacentElement (moderne)
container.insertAdjacentElement('beforebegin', div); // avant le container
container.insertAdjacentElement('afterbegin', div);  // premier enfant
container.insertAdjacentElement('beforeend', div);   // dernier enfant
container.insertAdjacentElement('afterend', div);    // après le container

// --- Supprimer des éléments ---
div.remove();                             // se supprimer soi-même
container.removeChild(div);              // supprimer un enfant

// --- Cloner des éléments ---
const clone = div.cloneNode(true);       // true = clone profond (avec les enfants)

// --- Remplacer des éléments ---
container.replaceChild(newNode, oldNode);
oldNode.replaceWith(newNode);            // moderne, plus simple

// --- Déplacer des éléments ---
// Insérer un nœud déjà attaché le déplace automatiquement
document.querySelector('#autre').appendChild(div);
```

---

## 🔌 Requêtes HTTP avec XMLHttpRequest

La méthode originale (legacy) pour effectuer des requêtes HTTP asynchrones.

```javascript
// Requête GET
const xhr = new XMLHttpRequest();

xhr.open('GET', 'https://api.exemple.com/utilisateurs');
xhr.setRequestHeader('Content-Type', 'application/json');

xhr.onreadystatechange = function () {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    if (xhr.status === 200) {
      const data = JSON.parse(xhr.responseText);
      console.log(data);
    } else {
      console.error('Erreur :', xhr.status);
    }
  }
};

xhr.onerror = function () {
  console.error('Erreur réseau');
};

xhr.send();

// Requête POST
const xhrPost = new XMLHttpRequest();
xhrPost.open('POST', 'https://api.exemple.com/utilisateurs');
xhrPost.setRequestHeader('Content-Type', 'application/json');

xhrPost.onload = function () {
  if (xhrPost.status === 201) {
    console.log('Créé :', JSON.parse(xhrPost.responseText));
  }
};

xhrPost.send(JSON.stringify({ nom: 'Alice', email: 'alice@exemple.com' }));
```

**Valeurs de readyState :**

| Valeur | État | Description |
|--------|------|-------------|
| 0 | UNSENT | `open()` pas encore appelé |
| 1 | OPENED | `open()` appelé |
| 2 | HEADERS_RECEIVED | `send()` appelé |
| 3 | LOADING | Réception des données |
| 4 | DONE | Requête terminée |

---

## 🚀 Requêtes HTTP avec Fetch API

Alternative moderne basée sur les Promises — plus claire et lisible que XHR.

```javascript
// Requête GET
fetch('https://api.exemple.com/utilisateurs')
  .then(response => {
    if (!response.ok) throw new Error(`Erreur HTTP : ${response.status}`);
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('Erreur :', error));

// GET avec async/await (recommandé)
async function getUtilisateurs() {
  try {
    const response = await fetch('https://api.exemple.com/utilisateurs');
    if (!response.ok) throw new Error(`Erreur HTTP : ${response.status}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Erreur :', error);
  }
}

// Requête POST
async function creerUtilisateur(userData) {
  const response = await fetch('https://api.exemple.com/utilisateurs', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer mon-token'
    },
    body: JSON.stringify(userData)
  });
  return response.json();
}

// PUT / DELETE suivent le même schéma
async function supprimerUtilisateur(id) {
  await fetch(`https://api.exemple.com/utilisateurs/${id}`, { method: 'DELETE' });
}
```

**Comparaison XHR vs Fetch :**

| Fonctionnalité | XMLHttpRequest | Fetch API |
|----------------|---------------|-----------|
| Syntaxe | Verbose, basée sur les callbacks | Propre, basée sur les Promises |
| Async/Await | ❌ | ✅ |
| Suivi de progression | ✅ | Limité |
| Support navigateur | Tous les navigateurs | IE11+ (avec polyfill) |
| Recommandé | Code legacy uniquement | ✅ Choix par défaut |

---

## Écouter les événements DOM

```javascript
const btn = document.querySelector('#submit-btn');

// --- addEventListener (recommandé) ---
btn.addEventListener('click', function (event) {
  console.log('Cliqué !', event);
});

// Syntaxe avec fonction fléchée
btn.addEventListener('click', (e) => {
  e.preventDefault();    // empêcher le comportement par défaut (soumission, lien…)
  e.stopPropagation();   // empêcher la propagation vers les éléments parents
  console.log('Cible :', e.target);
});

// --- Supprimer un écouteur (nécessite une fonction nommée) ---
function handleClick(e) {
  console.log('Cliqué');
}
btn.addEventListener('click', handleClick);
btn.removeEventListener('click', handleClick);

// --- Délégation d'événement (un seul écouteur pour plusieurs enfants) ---
document.querySelector('#liste').addEventListener('click', (e) => {
  if (e.target.matches('li')) {
    console.log('Élément cliqué :', e.target.textContent);
  }
});

// --- Écouteur à usage unique ---
btn.addEventListener('click', handler, { once: true });

// --- Événements DOM courants ---
document.addEventListener('DOMContentLoaded', () => console.log('DOM prêt'));
window.addEventListener('load', () => console.log('Page entièrement chargée'));
window.addEventListener('resize', () => console.log(window.innerWidth));
window.addEventListener('scroll', () => console.log(window.scrollY));
```

---

## 🖱️ Écouter les événements utilisateur

```javascript
// --- Événements souris ---
el.addEventListener('click', handler);        // clic simple
el.addEventListener('dblclick', handler);     // double clic
el.addEventListener('mouseenter', handler);   // curseur entre (sans propagation)
el.addEventListener('mouseleave', handler);   // curseur sort (sans propagation)
el.addEventListener('mouseover', handler);    // curseur survole (avec propagation)
el.addEventListener('mousedown', handler);    // bouton pressé
el.addEventListener('mouseup', handler);      // bouton relâché
el.addEventListener('contextmenu', handler);  // clic droit

// --- Événements clavier ---
document.addEventListener('keydown', (e) => {
  console.log('Touche pressée :', e.key, 'Code :', e.code);
  if (e.key === 'Enter') { /* … */ }
  if (e.ctrlKey && e.key === 's') { e.preventDefault(); sauvegarder(); }
});
document.addEventListener('keyup', handler);

// --- Événements formulaire / saisie ---
const input = document.querySelector('input');

input.addEventListener('input', (e) => {
  console.log('Valeur en direct :', e.target.value);  // déclenché à chaque frappe
});

input.addEventListener('change', (e) => {
  console.log('Valeur finale :', e.target.value); // déclenché au blur ou Entrée
});

input.addEventListener('focus', () => console.log('Champ actif'));
input.addEventListener('blur', () => console.log('Champ quitté'));

const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const data = new FormData(form);
  console.log(Object.fromEntries(data));
});

// --- Événements tactiles (mobile) ---
el.addEventListener('touchstart', handler);
el.addEventListener('touchend', handler);
el.addEventListener('touchmove', handler);
```

**Propriétés courantes des événements :**

| Propriété | Description |
|-----------|-------------|
| `e.target` | Élément qui a déclenché l'événement |
| `e.currentTarget` | Élément sur lequel l'écouteur est attaché |
| `e.type` | Nom de l'événement (`"click"`, `"keydown"`…) |
| `e.key` | Nom de la touche pour les événements clavier |
| `e.clientX/Y` | Coordonnées de la souris (relatives au viewport) |
| `e.preventDefault()` | Annule le comportement par défaut du navigateur |
| `e.stopPropagation()` | Stoppe la propagation vers les parents |

---

## 📚 Ressources

- [MDN — Introduction au DOM](https://developer.mozilla.org/fr/docs/Web/API/Document_Object_Model/Introduction)
- [MDN — Fetch API](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API)
- [MDN — EventTarget.addEventListener](https://developer.mozilla.org/fr/docs/Web/API/EventTarget/addEventListener)
- [javascript.info — Le DOM](https://javascript.info/document)

---

*Moulard Arthur*, 