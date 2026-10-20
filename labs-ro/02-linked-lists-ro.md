# Laboratorul 2: Linked Lists

## Implementează un stack și o structură queue în C

Rezolvă această cerință local, fără LeetCode. Folosește un linked list pentru
fiecare structură.

- Stack: implementează `push`, `pop`, `peek` și `is_empty`. Folosește ordinea
  LIFO: ultima valoare adăugată este prima valoare eliminată.
- Queue: implementează `enqueue`, `dequeue`, `front` și `is_empty`. Folosește
  ordinea FIFO: prima valoare adăugată este prima valoare eliminată.
- Tratează cazurile în care încerci să elimini sau să citești un element
  dintr-o structură goală.
- Eliberează memoria pentru node-urile eliminate și pentru toate node-urile
  rămase înainte de încheierea programului.
- Testează o structură goală, o structură cu o valoare și una cu mai multe
  valori. Elimină toate valorile, apoi adaugă din nou o valoare.
- Adaugă `4`, `7` și `2` în această ordine. Verifică dacă stack-ul elimină
  `2`, `7`, `4`, iar structura queue elimină `4`, `7`, `2`.

## Rezolvă aceste probleme LeetCode

Urmează pașii pentru cont și trimiterea soluției din
[Laboratorul 1](../labs/01-arrays.md).

1. [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
2. [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)
3. [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## Recomandări

1. Pentru fiecare problemă, fă cel puțin 3-5 încercări de trimitere a soluției
   înainte să ceri ajutor, dacă soluția nu este acceptată mai devreme. Nu
   consulta soluții și nu folosi AI în timpul acestor încercări.
2. Deschide fila **Solutions** numai **după** ce ai o soluție care funcționează
   și este acceptată. Compară alte abordări cu propriul cod.
3. **Opțional:** După ce soluția funcționează, cere unui AI să îți verifice
   codul și să propună îmbunătățiri.
