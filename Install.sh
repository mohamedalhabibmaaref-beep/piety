#!/bin/bash

echo "🏛️ [ جاري تطهير البيئة وتهيئة مِحْراب الراعي ] ⚔️"

# 1. كسر قيود النظام وتثبيت المكتبات الضرورية
echo "📡 جاري تثبيت المكتبات (تجاوز الحماية)..."
pip install gspread google-auth requests --break-system-packages

# 2. ضمان وجود المجلد السيادي في مكان ثابت
mkdir -p ~/piety

# 3. نقل الملفات الحيوية إلى موضعها الصحيح
cp piety_cli.py ~/piety/ 2>/dev/null

# 4. إعطاء صلاحيات التنفيذ لنخاع النظام
chmod +x ~/piety/piety_cli.py

# 5. تعميد الأمر 'piety' في سجل النظام (Alias)
# يتم الفحص أولاً لمنع التكرار في ملف الـ .bashrc
if ! grep -q "alias piety=" ~/.bashrc; then
    echo "alias piety='python3 ~/piety/piety_cli.py'" >> ~/.bashrc
fi

# 6. تفعيل التغيير فوراً
source ~/.bashrc

echo "--------------------------------------------------"
echo "✅ تم التثبيت بنجاح يا حامي السيادة!"
echo "🏛️ الآن، أعد تشغيل الترمينال أو اكتب: exec bash"
echo "⚔️ ثم اطلب الراعي بكتابة: piety"
echo "--------------------------------------------------"
