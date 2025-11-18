# מדריך מהיר — Benchmark ל-ATS (עברית)

מטרה: חבילה מוכנה להפעלה בסיסית של בנצ'מארק על מערכת ATS ויצירת דוח תיקוף.

מיקום קבצים חשובים:
- `benchmark_resumes_50.json` — קובץ המקור (בעיקרון נמצא בשורש הפרוייקט)
- `edge_case_resumes.json` — מקרים קיצוניים
- `ats_validation_script.py` — סקריפט תיקוף (Python 3.7+)
- `dist/benchmark_package/` — חבילת ההפצה (כוללת `README_he.md`, `bulk_validate.py`, `run_benchmark.sh`)

דרישות מקדימות:
- Python 3.7 או חדש יותר
- ATS שמאפשר ייבוא JSON וייצוא תוצרי חילוץ כקבצי JSON

שלבי הרצה מהירים:

1. העתק/וודא ש-`benchmark_resumes_50.json` קיים בשורש הריפו (או בתיקייה נוחה).

2. ייבוא ל-ATS:
   - ייבא את `benchmark_resumes_50.json` למערכת ה-ATS שלכם.
   - ודאו שכל 50 הקורות חיים נטענו בהצלחה.

3. הרצת חילוץ ב-ATS:
   - הריצו את פרסר/החילוץ של ה-ATS על כל הקבצים.
   - ייצאו את תוצרי החילוץ כקבצי JSON (אחד לכל קורות חיים) לתיקייה `dist/benchmark_package/ats_output/`.

4. הרצת תיקוף אוטומטי (בתיקיית החבילה):

```bash
cd dist/benchmark_package
./run_benchmark.sh
```

או להרצה ישירה של הסקריפט:

```bash
python3 bulk_validate.py ../../benchmark_resumes_50.json ats_output/ validation_report.json
```

5. פלט ותוצרים:
- `dist/benchmark_package/validation_report.json` — דוח סיכומי עם מדדי דיוק, F1 לכישורים, רשימת בעיות והמלצות.

6. בדיקת מקרים קיצוניים (אופציונלי):
   - ייבאו את `edge_case_resumes.json` ל-ATS והריצו את אותו תהליך כדי לבדוק טיפול במצבים בעיתיים.

אריזת החבילה להורדה:

```bash
cd dist/benchmark_package
zip -r ../../benchmark_package.zip . -x "*/__pycache__/*"
```

הערות למפתחים:
- `ats_validation_script.py` מכיל את המחלקות `ResumeValidator` ו-`BenchmarkRunner` שניתן להשתמש בהן בתרחישי בדיקה מותאמים.
- תיעוד סכמות ופורמט נמצא ב-`benchmark_documentation.json`.

רוצה שאארז עבורך את ה-zip עכשיו ואצרף כאן קישור להורדה מה-workspace? או להכין גם גרסה באנגלית של ה-README?
