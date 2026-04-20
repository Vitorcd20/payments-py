# PIX Payment API

REST API para geração e confirmação de pagamentos via PIX, com suporte a QR Code e notificações em tempo real via WebSocket.

![Python](https://img.shields.io/badge/Python-3-blue) ![Flask](https://img.shields.io/badge/Flask-green) ![SQLite](https://img.shields.io/badge/SQLite-SQLAlchemy-orange)

---

## Instalação

```bash
git clone <repo-url>
cd <projeto>
pip install flask flask-socketio flask-sqlalchemy

python app.py
```

A aplicação roda por padrão em `http://127.0.0.1:5000` com debug ativado.

---

## Endpoints

### `POST /payments/pix`
Cria um novo pagamento PIX com QR Code e validade de 30 minutos.

**Body:**
```json
{ "value": 49.90 }
```
**Resposta:**
```json
{ "message": "The payment has been created", "payment": { ... } }
```

---

### `GET /payments/pix/{payment_id}`
Renderiza a página do pagamento com QR Code ou tela de confirmação, se já pago.

---

### `GET /payments/pix/qr_code/{file_name}`
Retorna a imagem PNG do QR Code associado ao pagamento.

---

### `POST /payments/pix/confirmation`
Confirma um pagamento PIX recebido pelo banco e emite evento WebSocket ao cliente.

**Body:**
```json
{ "bank_payment_id": "abc123", "value": 49.90 }
```
**Evento emitido:** `payment-confirmed-{payment_id}`

---

## WebSocket

Ao confirmar um pagamento, o servidor emite um evento em tempo real para o cliente monitorar o status.

```javascript
const socket = io("http://127.0.0.1:5000");
socket.on("payment-confirmed-42", () => {
  console.log("Pagamento confirmado!");
});
```

---

## Estrutura de pastas
