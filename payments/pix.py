import uuid, qrcode

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self):
        # criar pagamento na instituição financeira
        bank_payment_id = uuid.uuid4()
        
        # copia e cola
        hash_payment = f'hash_payment_{bank_payment_id}'
        
        # qr code
        img = qrcode.make(hash_payment)
        
        # salvar como arq png
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")
        
        
        return {"payment_bank_id": bank_payment_id, "qr_code_path": f"qr_code_payment_{bank_payment_id}"}