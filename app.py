from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# دالة لقراءة أو إنشاء ملف Excel وتخزين البيانات فيه
def save_to_excel(tenant_name, land_paper, plot_number, feddan, qirat, share, violations):
    # تحديد اسم ملف Excel
    file_name = 'tenants.xlsx'

    # إذا كان الملف موجودًا مسبقًا، نقرأ البيانات منه
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
    else:
        # إذا كان الملف غير موجود، ننشئ DataFrame جديد
        df = pd.DataFrame(columns=['tenant_name', 'land_paper', 'plot_number', 'feddan', 'qirat', 'share', 'violations'])

    # إضافة البيانات الجديدة إلى DataFrame
    new_data = {
        'tenant_name': tenant_name,
        'land_paper': land_paper,
        'plot_number': plot_number,
        'feddan': feddan,
        'qirat': qirat,
        'share': share,
        'violations': violations
    }
    df = df.append(new_data, ignore_index=True)

    # حفظ التغييرات في ملف Excel
    df.to_excel(file_name, index=False)

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# دالة لإضافة المستأجر إلى ملف Excel
@app.route('/add_tenant', methods=['POST'])
def add_tenant():
    if request.method == 'POST':
        tenant_name = request.form['tenant_name']
        land_paper = request.form['land_paper']
        plot_number = request.form['plot_number']
        feddan = int(request.form['feddan'])
        qirat = int(request.form['qirat'])
        share = int(request.form['share'])
        violations = request.form['violations']
        
        # تخزين البيانات في ملف Excel
        save_to_excel(tenant_name, land_paper, plot_number, feddan, qirat, share, violations)
        
        return redirect(url_for('index'))

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)
