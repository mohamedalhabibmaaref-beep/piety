#!/bin/bash

echo "⚔️ [جاري تنصيب محراب السلطان Piety C1.0] ⚔️"
echo "بإشراف: محمد الحبيب (المصمم السيادي)"

# 1. تحديث وتثبيت المتطلبات الأساسية
pkg update -y && pkg upgrade -y
pkg install python python-requests curl git -y

# 2. تنزيل Ollama (المحرك النخاعي) لإصدارات ARM64 (أندرويد)
echo "📦 جاري استدعاء المحرك Ollama..."
curl -L https://ollama.com/download/ollama-linux-arm64.tgz -o ollama.tgz
tar -xzf ollama.tgz && rm ollama.tgz
mv ollama $PREFIX/bin/

# 3. جلب سكريبت Piety ووضعه في النظام
echo "📜 جاري تحميل بروتوكول Piety..."
curl -sL https://raw.githubusercontent.com/mohamedalhabibmaaref-beep/piety/main/piety.py -o $PREFIX/bin/piety
chmod +x $PREFIX/bin/piety

# 4. إعداد المجلد السيادي
mkdir -p ~/Sovereign_Drive
echo "مرحباً بك في مصفوفتك الخاصة. ضع ملفاتك هنا ليحللها الراعي." > ~/Sovereign_Drive/README.txt

echo "✅ اكتمل التثبيت يا ملك!"
echo "------------------------------------------------"
echo "1️⃣  افتح جلسة جديدة واكتب: ollama serve"
echo "2️⃣  عد هنا واكتب: piety"
echo "------------------------------------------------"
