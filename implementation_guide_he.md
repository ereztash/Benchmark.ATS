# ATS Benchmark Dataset - הוראות יישום מלאות

## 📋 סקירה כללית

מאגר זה מכיל **50 קורות חיים בפורמט JSON** המעוצבים להיות מבחן בנצ'מארק (benchmark) אמין למערכות ATS (Applicant Tracking Systems). המאגר כולל:

- ✅ **12 קטגוריות תפקידים** (סוֹפטוויֵר, Product, Data, Marketing, HR וכו')
- ✅ **4 רמות סניוריות** (Junior → Lead)
- ✅ **וריאציות מגוונות**: פערים בעבודה, מעברי קריירה, סוגי שגיאות בנתונים
- ✅ **גיוון גיאוגרפי**: 10 ערים בישראל
- ✅ **פילוג שפות**: ערבוב עברית-אנגלית ריאליסטי

---

## 🗂️ הקבצים שנוצרו

| קובץ | תוכן | גודל |
|------|------|------|
| **benchmark_resumes_50.json** | 50 קורות חיים מלאות בפורמט JSON Resume v1.0.0 | 117.1 KB |
| **benchmark_documentation.json** | תיעוד מלא של סכמה וויזואליזציה | JSON |
| **benchmark_resume_examples.json** | 12 דוגמאות מפורטות של וריאציות | JSON |
| **edge_case_resumes.json** | 8 תרחישים בעיתיים לבדיקת עמידות | JSON |
| **ats_validation_script.py** | סקריפט Python לבדיקת דיוק וחילוץ נתונים | Python |
| **ats_testing_guide.json** | הוראות בדיקה מלאות ותבנית דוח | JSON |
| **benchmark_summary.json** | סיכום ושדה ביקורת | JSON |

---

## 🚀 תהליך בדיקה שלב אחר שלב

### שלב 1: הכנה והטעינה
```
1. הורד את benchmark_resumes_50.json
2. טעון אל תוך מערכת ה-ATS שלך
3. ודא שכל 50 הקורות חיים התקבלו בהצלחה
4. ביצע סנכרון מלא של הנתונים
```

### שלב 2: הפעלת חילוץ הנתונים
```
1. בצע ניתוח מלא של כל 50 הקורות חיים
2. אפשר לכל תכני ATS שלך להפעיל את אלגוריתם הניתוח
3. עקוב אחר זמן העיבוד (יעד: <500ms לכל קורות חיים)
4. תעד את כל הנוציא או הודעות שגיאה
```

### שלב 3: ייצוא הנתונים המוצגים
```
1. ייצא את הנתונים המוצגים מה-ATS (שדות חילוץ מלאים)
2. שמור בפורמט JSON או CSV
3. ודא שלפחות השדות הבאים זמינים:
   - Name, email, phone
   - Company, position, dates
   - Skills list
   - Education history
4. הערה: השם קבצים המייצגים כל קורות חיים בצורה ייחודית
```

### שלב 4: הרצת בדיקת תיקיוף
```bash
# הרץ את סקריפט הבדיקה
python ats_validation_script.py benchmark_resumes_50.json ats_output_folder/

# פלט מצפה:
# - accuracy report per field
# - precision/recall for skills
# - issues list
# - recommendations
```

### שלב 5: ניתוח התוצאות
```
1. סקור את דוח הדיוק (accuracy report)
2. זהה אתגרים בנושאים שונים (basics, work, education, skills)
3. בחן את תוצאות מקרי הקצה (edge cases)
4. זהה דפוסים בשגיאות
```

### שלב 6: בדיקת מקרים קיצוניים
```
1. טעון את edge_case_resumes.json
2. בצע ניתוח ייעודי על 8 המקרים הקיצוניים
3. ודא טיפול חן בשגיאות ללא התמוטטויות
4. בדוק:
   - Handling of employment gaps
   - Overlapping employment dates
   - Special Hebrew characters
   - Future dates detection
   - Keyword stuffing flags
```

---

## 📊 מדדי הצלחה - קריטריונים

### מדדי קו בסיס (Baseline Metrics)

| מדד | היעד | הערות |
|-----|------|-------|
| **דיוק כללי** | ≥ 92% | ממוצע משוקלל על כל השדות |
| **ניתוח Basics** | ≥ 95% | שם, אימייל, טלפון וכו' |
| **ניתוח Work** | ≥ 93% | שם חברה, תפקיד, תאריכים |
| **ניתוח Education** | ≥ 95% | מוסד, תואר, שנים |
| **F1 Score Skills** | ≥ 87% | Precision × Recall |
| **דיוק תאריכים** | ≥ 98% | תאריכים שנחלצו בצורה נכונה |
| **טיפול שגיאות** | ✅ כן | אין קריסות או שגיאות קטלניות |
| **מהירות עיבוד** | < 500ms | לכל קורות חיים |

---

## 🔍 וריאציות קורות חיים כלולות

### 1. High Keyword Density (~5 resumes)
**מטרה**: בדוק זיהוי של אופטימיזציה יתרה לנועדת מחוברים חיפוש
- קורות חיים עם חזרות מילים-מפתח
- דגלון: זה אדום עבור חלק מהמעסיקים

### 2. Employment Gaps (~8 resumes)
**מטרה**: בדוק זיהוי של פערים בתעסוקה
- פערים של 6-18 חודשים בין משרות
- תרחיש: לידה, השכלה, אבטלה, או אחר

### 3. Career Transitions (~6 resumes)
**מטרה**: בדוק מיפוי כישורים תוך-תחומיים
- הנדסה → Product Manager
- מכירות → Marketing
- יעדה כישורים הניתנים להעברה

### 4. Job Hopping (~5 resumes)
**מטרה**: בדוק זיהוי דפוסי שינוי תדיר של משרות
- ממוצע קבע: 6-10 חודשים למשרה
- דגל: חוסר יציבות אפשרי

### 5. Fresh Graduates (~3 resumes)
**מטרה**: בדוק הטיפול בקורות חיים חדשים-בטר ללא ניסיון
- אין היסטוריה מקצועית
- דגש על חינוך ופרויקטים אוניברסיטאיים

### 6. Self-Taught Professionals (~3 resumes)
**מטרה**: בדוק בחירוח על בחינה בלתי-מסורתית
- אין תואר פורמאלי
- קורסים מקוונים + ניסיון עבודה

### 7. Long Tenure Stability (~4 resumes)
**מטרה**: בדוק הכרה בקידום קריירה בתוך חברה אחת
- 8 שנות מקיפות בחברה אחת
- עלייה: Junior → Manager

### 8. Special Characters & Hebrew (~8 resumes)
**מטרה**: בדוק טיפול בעברית וסימנים מיוחדים
- שמות בעברית (א-ת כו')
- תווי מיוחדים (קו נטיה, גרש וכו')

### 9. Data Quality Errors (~8 resumes)
**מטרה**: בדוק גילוי שגיאות וביעוח
- תאריכים בעתיד (2026)
- תאריכים חופפים
- שדות חסרים בכוונה

### 10. Language Quality Variations (~15 resumes)
**מטרה**: בדוק שהה לא-מובנים כלי-אנגלית (ESL)
- Native English (50%)
- ESL עם שגיאות קטנות (35%)
- ESL עם בעיות גדולות יותר (15%)

---

## 📋 תרחישי בדיקה ספציפיים

### תרחיש 1: התאמת מילות-מפתח
```
1. בחר 10 משרות לדוגמה (job postings)
2. הפעל את כל 50 הקורות חיים כנגד כל משרה
3. דוג התאמות המוצגות בדירוג (ranking)
4. בדוק: האם קורות חיים עם מילות-מפתח אמיתיות דורגים גבוה יותר?
```

### תרחיש 2: חילוץ כישורים
```
1. בדוק את קורות החיים #1-10
2. השווה כישורים מוצגים vs. כישורים במקור JSON
3. חשב precision/recall
4. זהה: False positives, Missed skills, Grouped skills
```

### תרחיש 3: חישוב שנות ניסיון
```
1. בדוק את כל תאריכי ההתחלה/סיום
2. חשב סה"כ שנות ניסיון רלוונטי
3. השווה ממוצע = משוקלל בהתאם לרלוונטיות
4. בדוק: Overlapping dates, Gaps, Edge cases
```

### תרחיש 4: סיווג רמת הכישרון
```
1. בדוק קורות חיים בדירוג שונה (Junior/Senior/Lead)
2. ודא שה-ATS מסווג בצורה נכונה
3. בדוק: האם עלויות מיומנות משפיעים על דרוג?
4. זהה: Bias towards specific titles
```

---

## ⚡ עיצוב דוח בדיקה

### נתונים להיות מוקדים בדוח הבדיקה

```json
{
  "test_date": "YYYY-MM-DD",
  "ats_system": "System Name v1.0",
  "test_summary": {
    "total_resumes_tested": 50,
    "successful_parses": 50,
    "failed_parses": 0,
    "average_accuracy": 94.2,
    "average_parse_time_ms": 342
  },
  "accuracy_by_field": {
    "basics": {
      "accuracy": 96.5,
      "fields": {
        "name": 100,
        "email": 100,
        "phone": 95,
        "label": 92,
        "summary": 91
      }
    },
    "work": {
      "accuracy": 93.8,
      "issues": ["Missing highlights", "Date format mismatches"]
    },
    "education": {
      "accuracy": 94.2
    },
    "skills": {
      "precision": 89.3,
      "recall": 87.5,
      "f1_score": 88.4
    }
  },
  "edge_case_results": {
    "employment_gaps": "✅ Correctly identified",
    "overlapping_dates": "⚠️ Not flagged",
    "special_characters": "✅ Handled correctly",
    "future_dates": "❌ Not validated"
  },
  "critical_issues": [
    "Not detecting overlapping employment dates",
    "Hebrew characters causing encoding issues in 2 resumes"
  ],
  "recommendations": [
    "Improve overlapping date detection",
    "Fix Unicode/Hebrew character handling",
    "Enhance keyword relevance scoring"
  ]
}
```

---

## 🎯 סכום ביקורת

### חברה/מערכת מתחת לבדיקה
___________________

### תאריך בדיקה
___________________

### שם בודק
___________________

### ממצאים עיקריים
- [ ] דיוק >= 92%?
- [ ] לא כשלים בעיבוד?
- [ ] טיפול תקין בקצה-cases?
- [ ] מהירות < 500ms/resume?

### בעיות המצאות לעבודה
1. ___________________
2. ___________________
3. ___________________

### צעדי הפתרון המוצעים
1. ___________________
2. ___________________
3. ___________________

### עוקב בתאריך
___________________

---

## 💡 טיפים לשימוש

1. **ערוך שמות קבצים ייחודיים**: סובב כל קורות חיים עם ID ייחודי (resume_001.json)
2. **וודא עקביות**: בדוק שנהלי השחקנים זהים על כל 50 הקורות חיים
3. **בדוק שנית**: בצע הפעלה שנייה של אותו סט כדי לוודא עקביות
4. **עקוב בתיעוד**: שמור על כל השגיאות וההודעות לעיון חוקרי

---

## 📞 תמיכה והחזקה

- **יצירת JSON**: נוצר בעזרת Python + JSON Resume standard v1.0.0
- **תיקוף**: ההפעלה בתמיכה Python 3.7+
- **שונות לעתיד**: ניתן להוסיף וריאציות נוספות או עדכן הערות

---

**גרסה**: 1.0  
**תאריך ביצוע**: 2025-11-18  
**סטנדרט סכמה**: JSON Resume v1.0.0
