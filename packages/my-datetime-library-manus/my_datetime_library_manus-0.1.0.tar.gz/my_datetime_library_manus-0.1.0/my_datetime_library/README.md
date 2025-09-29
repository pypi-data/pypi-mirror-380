# مكتبة الوقت والتاريخ المخصصة (my_datetime_library)

هذه مكتبة بايثون مخصصة للتعامل مع الوقت والتاريخ بدقة عالية، تم بناؤها من الصفر دون الاعتماد على مكتبات بايثون المدمجة مثل `datetime` أو `time` أو `pytz`. تهدف المكتبة إلى توفير تحكم دقيق في حسابات الوقت، بما في ذلك دعم التوقيت الذري الدولي (TAI) والتوقيت العالمي المنسق (UTC) والثواني الكبيسة، بالإضافة إلى التعامل مع المناطق الزمنية.

## الميزات الرئيسية (المخطط لها/المنفذة جزئياً)

*   **دقة النانوثانية:** جميع العمليات تتم بدقة النانوثانية لضمان أعلى مستوى من الدقة.
*   **دعم TAI و UTC:** التعامل مع مقياسي الوقت TAI و UTC، بما في ذلك التحويلات بينهما مع الأخذ في الاعتبار الثواني الكبيسة.
*   **الثواني الكبيسة:** إدارة الثواني الكبيسة باستخدام بيانات IANA Time Zone Database.
*   **المناطق الزمنية:** دعم المناطق الزمنية باستخدام بيانات IANA Time Zone Database (قيد التطوير).
*   **عمليات حسابية قوية:** جمع وطرح النقاط الزمنية والمدد الزمنية.
*   **تمثيل واضح:** كائنات `TimePoint` لتمثيل لحظات محددة في الزمن، وكائنات `Duration` لتمثيل الفترات الزمنية.

## الهيكل الأساسي للمكتبة

تتكون المكتبة من الوحدات الرئيسية التالية:

*   `timepoint.py`: يحدد الكلاس `TimePoint` لتمثيل لحظة معينة في الزمن، و `TimeScale` (TAI/UTC).
*   `duration.py`: يحدد الكلاس `Duration` لتمثيل فترة زمنية.
*   `calendar_utils.py`: يحتوي على وظائف مساعدة لحسابات التقويم (مثل تحديد السنوات الكبيسة وعدد الأيام في الشهر).
*   `leap_seconds.py`: يدير جدول الثواني الكبيسة ويقدم وظائف للحصول على فرق TAI-UTC.
*   `timezone.py`: يحدد الكلاس `TimeZone` و `TimeZoneDatabase` للتعامل مع المناطق الزمنية (قيد التطوير).
*   `constants.py`: يحتوي على الثوابت المشتركة المستخدمة في جميع أنحاء المكتبة.

## التثبيت (مستقبلاً)

بمجرد أن تصبح المكتبة جاهزة، ستكون متاحة للتثبيت عبر `pip`:

```bash
pip install my_datetime_library
```

## الاستخدام

### إنشاء `TimePoint`

يمكن إنشاء `TimePoint` من مكونات التاريخ والوقت:

```python
from my_datetime_library import TimePoint, TimeScale

# إنشاء نقطة زمنية في مقياس TAI
tp_tai = TimePoint.from_components(2023, 10, 27, 15, 30, 0, 0, time_scale=TimeScale.TAI)
print(f"TimePoint (TAI): {tp_tai}")
print(f"Components (TAI): {tp_tai.to_components()}")

# إنشاء نقطة زمنية في مقياس UTC
tp_utc = TimePoint.from_components(2023, 10, 27, 15, 30, 0, 0, time_scale=TimeScale.UTC)
print(f"TimePoint (UTC): {tp_utc}")
print(f"Components (UTC): {tp_utc.to_components()}")
```

### إنشاء `Duration`

يمكن إنشاء `Duration` من الثواني أو الدقائق أو الساعات أو الأيام:

```python
from my_datetime_library import Duration

duration_seconds = Duration.from_seconds(3600) # ساعة واحدة
print(f"Duration (seconds): {duration_seconds.to_seconds()} seconds")

duration_days = Duration.from_days(7) # 7 أيام
print(f"Duration (days): {duration_days.to_days()} days")
```

### العمليات الحسابية

يمكن جمع وطرح `Duration` من `TimePoint`، وطرح `TimePoint` من `TimePoint` للحصول على `Duration`:

```python
from my_datetime_library import TimePoint, Duration, TimeScale

tp = TimePoint.from_components(2023, 10, 27, 10, 0, 0, time_scale=TimeScale.UTC)
duration = Duration.from_hours(3)

tp_plus_duration = tp + duration
print(f"TimePoint + Duration: {tp_plus_duration.to_components()}")

tp_minus_duration = tp - duration
print(f"TimePoint - Duration: {tp_minus_duration.to_components()}")

tp_later = TimePoint.from_components(2023, 10, 27, 15, 0, 0, time_scale=TimeScale.UTC)
diff_duration = tp_later - tp
print(f"Difference between TimePoints (hours): {diff_duration.to_hours()}")
```

### التعامل مع الثواني الكبيسة والتحويل بين TAI و UTC

تتطلب هذه العمليات تحميل جدول الثواني الكبيسة:

```python
from my_datetime_library import TimePoint, TimeScale, LeapSecondTable
import os

# يجب أن يكون ملف leap-seconds.list متاحاً في المسار الصحيح
# (على سبيل المثال، في نفس المجلد أو مجلد الجذر للمشروع)
leap_second_file_path = "leap-seconds.list" # افترض أن الملف موجود هنا

if os.path.exists(leap_second_file_path):
    ls_table = LeapSecondTable()
    ls_table.load_from_file(leap_second_file_path)

    # مثال: تحويل من TAI إلى UTC
    # لنفترض أن 1972-01-01 00:00:10 TAI هو 1972-01-01 00:00:00 UTC (مع 10 ثواني كبيسة)
    tai_tp = TimePoint.from_components(1972, 1, 1, 0, 0, 10, time_scale=TimeScale.TAI)
    utc_tp = tai_tp.to_utc(ls_table)
    print(f"TAI TimePoint: {tai_tp.to_components()} -> UTC TimePoint: {utc_tp.to_components()}")

    # مثال: تحويل من UTC إلى TAI
    utc_tp_2017 = TimePoint.from_components(2017, 1, 1, 0, 0, 0, time_scale=TimeScale.UTC)
    tai_tp_2017 = utc_tp_2017.to_tai(ls_table)
    print(f"UTC TimePoint: {utc_tp_2017.to_components()} -> TAI TimePoint: {tai_tp_2017.to_components()}")
else:
    print(f"تحذير: ملف الثواني الكبيسة ​`{leap_second_file_path}`​ غير موجود. لا يمكن اختبار تحويلات TAI/UTC.")
```

### التعامل مع المناطق الزمنية (قيد التطوير)

```python
from my_datetime_library import TimePoint, TimeScale, TimeZoneDatabase
import os

# يجب أن تكون ملفات tzdata (مثل zone.tab) متاحة في المسار الصحيح
# (على سبيل المثال، في مجلد الجذر للمشروع)
tzdata_directory = "." # افترض أن الملفات موجودة هنا

tzdb = TimeZoneDatabase()
tzdb.load_from_tzdata_files(tzdata_directory)

ny_zone = tzdb.get_timezone("America/New_York")
if ny_zone:
    utc_tp = TimePoint.from_components(2023, 10, 27, 12, 0, 0, time_scale=TimeScale.UTC)
    
    # الحصول على الإزاحة والاختصار للمنطقة الزمنية
    offset_seconds, abbr = ny_zone.get_total_offset_and_abbr(utc_tp)
    print(f"America/New_York offset: {offset_seconds / 3600} hours, Abbr: {abbr}")

    # تحويل UTC إلى الوقت المحلي
    local_tp_ny = ny_zone.localize(utc_tp)
    print(f"UTC: {utc_tp.to_components()} -> Local (NY): {local_tp_ny.to_components()}")

    # تحويل الوقت المحلي إلى UTC
    unlocalized_tp = ny_zone.unlocalize(local_tp_ny)
    print(f"Local (NY): {local_tp_ny.to_components()} -> UTC: {unlocalized_tp.to_components()}")
else:
    print(f"تحذير: المنطقة الزمنية America/New_York غير موجودة في قاعدة البيانات المبسطة.")
```

## المساهمة

نرحب بالمساهمات! يرجى قراءة `CONTRIBUTING.md` (مستقبلاً) للحصول على إرشادات.

## الترخيص

هذه المكتبة مرخصة بموجب ترخيص MIT. انظر ملف `LICENSE` لمزيد من التفاصيل.



## تحسين الأداء (خطط مستقبلية)

*   **البحث الثنائي:** حاليًا، تعتمد وظائف البحث عن الثواني الكبيسة وقواعد المناطق الزمنية على البحث الخطي. يمكن تحسين الأداء بشكل كبير باستخدام البحث الثنائي (Binary Search) نظرًا لأن البيانات مرتبة حسب الوقت.
*   **التخزين المؤقت (Caching):** يمكن تطبيق آليات التخزين المؤقت للنتائج المتكررة للحسابات المعقدة، مثل تحويلات TAI/UTC لنقاط زمنية متقاربة.
*   **تحسين هياكل البيانات:** مراجعة هياكل البيانات المستخدمة لتخزين القواعد والبيانات لضمان الكفاءة المثلى من حيث الذاكرة والسرعة.
*   **التحسينات على مستوى C (اختياري):** في المستقبل، قد يتم النظر في إعادة كتابة الأجزاء الحساسة للأداء بلغة C أو Rust لزيادة السرعة.

