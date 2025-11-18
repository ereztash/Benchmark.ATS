# חבילת Benchmark ל-ATS — מדריך מהיר

מטרה: להריץ במהירות את הבנצ'מארק על מערכת ATS ולייצר דוח דיוק.

תכולה של החבילה:
- `benchmark_resumes_50.json` — מאגר 50 קורות חיים (יש להעביר לתיקיית החבילה לפני הריצה)
- `edge_case_resumes.json` — 8 מקרים קיצוניים לבדיקה
- `ats_validation_script.py` — סקריפט בדיקה והערכה (Python 3.7+)
- `ats_testing_guide.json` — הוראות בדיקה מפורטות
- `implementation_guide_he.md` — מדריך בעברית (פרטים נוספים)
- `run_benchmark.sh` — סקריפט עזר להרצה מהירה

דרישות מקדימות:
- Python 3.7 או חדש יותר (הסקריפט משתמש בספריות סטנדרטיות בלבד).
- גישה ל-ATS: דרך ממשק שמאפשר ייבוא/ייצוא של קורות חיים בפורמט JSON.

שלבי הרצה קצרים:
1. העתק את הקבצים הבאים לתיקייה נוחה על המחשב שבו תריצו את הבדיקה:
   - `benchmark_resumes_50.json`
   - `edge_case_resumes.json`
   - `ats_validation_script.py`

2. טעינת קורות החיים ל-ATS
   - ייבא את `benchmark_resumes_50.json` למערכת ה-ATS שלכם לפי הוראות המערכת.
   - בדקו שכל 50 הקבצים נטענו בהצלחה.

3. הפעלת חילוץ ב-ATS
   - הריצו את מנגנון החילוץ/פרסינג של ה-ATS על כל הקבצים.
   - ייצאו את תוצרי החילוץ (extracted outputs) כקבצי JSON לכל קורות החיים, בתיקייה בשם `ats_output/`.

4. הרצת סקריפט התיקוף
   - ודאו שאתם בתיקייה שמכילה `ats_validation_script.py` ו-`benchmark_resumes_50.json`.
   - הריצו את הפקודה:

```bash
python3 ats_validation_script.py benchmark_resumes_50.json ats_output/
```

   - הפלט יהיה דוח דיוק (JSON) עם מדדי accuracy, precision/recall לכישורים, רשימת בעיות והמלצות.

5. בדיקת מקרים קיצוניים (אופציונלי)
   - ייבאו את `edge_case_resumes.json` ל-ATS והריצו אותו כנפרד כדי לאמת טיפול בשגיאות.

6. חבילה להורדה
   - כדי לארוז את החבילה להורדה, ניתן להריץ:

```bash
cd dist/benchmark_package
zip -r benchmark_package.zip .
```

תמיכה ופרטים נוספים:
- לעיון מעמיק בעברית, פתחו את `implementation_guide_he.md`.
- למפתחים: לפרטי הסכמה ופורמט השתמשו ב-`benchmark_documentation.json` ו-`file_index_and_reference.json`.

גרסה: 1.0 — תאריך: 2025-11-18
