# 🧠 KkoScanner — Project Notes (Foam)

## 1. Obiettivo del progetto

- Strumento: port scanner TCP/UDP “Nmap-like” minimale.
- Target: studio personale + base per futuri tool di pentesting.
- Focus attuale:
  - Separare logica di **scan** da logica di **risposta**.
  - Introdurre `send_response` senza rompere `sorted_dict`.
  - Preparare il terreno per una revisione seria del modello di thread.

---

## 2. Architettura attuale (v0)

- Modulo principale:
  - `open_scan(port, flag_set, scan_data, ...)`
- Funzioni correlate:
  - `read_response(...)`
  - `packet_craft(...)`
- Strutture dati chiave:
  - `scan_data.sorted_dict` → risultati “ufficiali” dello scan.
  - `scan_data` (campi attuali + campi da aggiungere).
- Limiti noti:
  - Eccezioni di invio pacchetti finiscono dentro `sorted_dict`.
  - Mancanza di separazione tra:
    - **risultato logico di porta (open/closed/filtered)**  
    - **errori di trasporto (socket, invio pacchetto, retry fallito)**

---

## 3. Nuova funzione: `send_response` (design)

### 3.1. Ruolo

- Funzione “gemella” di `open_scan` usata per:
  - inviare ACK/FIN/RST (e in futuro altri flag) in risposta a pacchetti ricevuti.
- Deve:
  - Riutilizzare la stessa logica di:
    - creazione socket
    - invio pacchetto
    - retry con `attempt` + `time.sleep(0.2)`
  - NON modificare `sorted_dict`.
  - Scrivere SOLO in una struttura di errori dedicata.

### 3.2. Firma prevista (concettuale)

- Parametri essenziali:
  - `target_ip`
  - `port`
  - `flag_set` (ACK/FIN/RST…)
  - `scan_data` (per accedere a IP locale, timeout, error_response, ecc.)
- Return:
  - `None` oppure un booleano `True/False` per “inviato / fallito” (da decidere).

### 3.3. Requisiti di comportamento

- Deve rispettare:
  - max 3 tentativi con delay.
  - gestione eccezioni locale, senza “sporcare” il flusso di scan.
- Collegamento con half-open scan:
  - L’ACK inviato non è “gratis”: in futuro potremmo voler leggere e loggare la reazione del target.

---

## 4. Nuova struttura errori: `scan_data.error_response`

### 4.1. Scopo

- Contenere solo:
  - errori di invio pacchetto in `open_scan`
  - errori di invio risposta in `send_response`
- Mai usata per:
  - decidere stato logico della porta (questo resta in `sorted_dict`).

### 4.2. Struttura dati (concettuale)

- Dizionario:
  - chiave: `port`
  - valore: lista/dizionario di dettagli dell’errore.
- Esempio concettuale:
  - `scan_data.error_response[port] = [f"Failed to send {flag_set}", "attempts=3", "exception=str(e)"]`

### 4.3. Uso da parte dell’utente

- Non mostrata di default in `display_results`.
- Accessibile:
  - solo su richiesta (es: prompt “Vuoi vedere gli errori di invio pacchetti?”).
  - utile per debugging avanzato.

---

## 5. Politica di gestione errori

### 5.1. In `open_scan`

- Logica attuale (da migrare):
  - `attempt` + `time.sleep(0.2)`
  - dopo 3 tentativi:
    - prima: scriveva in `sorted_dict` → “Something went wrong…”
    - futuro: scriverà in `error_response` e lascerà `sorted_dict` immutato (o con valore neutro definito).

### 5.2. In `send_response`

- Stessa struttura di retry.
- Eccezioni:
  - non devono interrompere `read_response`.
  - non devono modificare `sorted_dict`.
  - creano un record in `error_response`.

### 5.3. In `read_response`

- Decide QUANDO:
  - chiamare `send_response`.
  - ignorare eventuali errori (salvati ma non bloccanti).
- In futuro:
  - potrà analizzare la reazione del target all’ACK/FIN/RST.

---

## 6. Modello di stato della porta (concettuale)

- Stati logici gestiti in `sorted_dict`:
  - `open`
  - `closed`
  - `filtered`
  - `open|filtered` (o simili, se implementati)
- Relazione con gli errori:
  - assenza di risposta ≠ errore di invio.
  - errore di invio è un problema di **strumento**, non di **target**.

---

## 7. Threading e concorrenza (revisione futura)

### 7.1. Situazione attuale

- Scansione multipla:
  - un thread per porta / per batch di porte (da confermare nel codice).
- Problema:
  - Gestione concorrente di:
    - socket
    - `sorted_dict`
    - futuri `error_response`

### 7.2. Idee per revisione

- Introdurre:
  - semaphore per sezioni critiche (ad es. update strutture globali).
  - coda di task per centralizzare l’invio di pacchetti “di risposta”.
- Obiettivo:
  - evitare race condition.
  - rendere il comportamento ripetibile tra run diversi.

---

## 8. Roadmap tecnica

### 8.1. Step immediati

- [X] Aggiungere `error_response` a `scan_data`.
- [X] Verificare se lo scan viene effettuate faccendo un shuffle di `scan_list`
- [ ] modificare la logica del riportare gli errori sia in sorted_dict solo errore bloccante che in error response errore bloccante, flag inviata
- [ ] Adattare `send_response` a usare `error_response` invece di `sorted_dict` per gli errori.
- [ ] modificare `open_scan` perché mostri solo l'ultimo errore bloccante ma alimenti i counter degli errori
- [ ] Definire la firma di `send_response`.
- [ ] Implementare `send_response` come copia 1:1 di `open_scan` con gestione errori diversa.
- [ ] Integrare `send_response` dentro `read_response` nei punti giusti.

### 8.2. Step successivi

- [ ] Rivedere il modello di threading.
- [ ] Introdurre logging opzionale (verbose/silent).
- [ ] Introdurre una modalità “debug” che mostra anche `error_response`.
- [ ] Documentare i principali casi limite (porte filtrate, RST strani, ecc.).

---

## 9. Appunti vari (area di lavoro libera)

- Qui puoi scrivere:
  - idee al volo
  - bug osservati durante i test
  - comandi usati per il debugging
  - differenze tra OS (Windows/Linux) se emergono
