#!/bin/bash

echo "🏛️ [ جاري تهيئة مِحْراب الراعي في نظامك ] ⚔️"

# 1. تثبيت المكتبات وتجاوز حماية النظام (مهم جداً للطلبة)
echo "📡 جاري تثبيت المكتبات..."
pip install gspread google-auth requests --break-system-packages

# 2. إنشاء المسار السيادي ونقل الملفات
echo "📂 جاري تنظيم المجلدات..."
mkdir -p ~/piety
cp piety_cli.py ~/piety/ 2>/dev/null

# 3. إعطاء صلاحيات التنفيذ لنخاع النظام
chmod +x ~/piety/piety_cli.py

# 4. تعميد الأمر 'piety' في نظام المستخدم
# نتحقق أولاً إذا كان الأمر موجوداً لعدم التكرار
if ! grep -q "alias piety=" ~/.bashrc; then
    echo "alias piety='python3 ~/piety/piety_cli.py'" >> ~/.bashrc
    echo "✅ تم إضافة الأمر piety إلى سجل النظام."
fi

# 5. تفعيل التغييرات فوراً في الجلسة الحالية
source ~/.bashrc

echo "--------------------------------------------------"
echo "🏛️ تم التثبيت بنجاح يا بطل!"
echo "⚠️  ملاحظة: إذا لم يعمل الأمر فوراً، اكتب: exec bash"
echo "ثم ابدأ السيادة بكتابة: piety"
echo "--------------------------------------------------"
