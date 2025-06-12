# yara1n

Эксплойт для iOS устройств в стиле palera1n/checkm8. (mb a12-a15 (??))

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
# Переход в DFU
python3 src/exploit.py dfu

# Переход в Recovery
python3 src/exploit.py recovery

# Перезагрузка
python3 src/exploit.py reboot
```

## Требования

- Python 3.6+
- pyusb
- iOS устройство в DFU режиме 