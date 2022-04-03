# تحليل ملف .wav للحصول على تردد أخذ العينات وعدد القنوات وعدد بتات التكميم وعدد نقاط أخذ العينات
import numpy as np
import sys
import wave   # حزمة معالجة ملف الصوت
import getopt

def main(argv):  # تحديد وظيفة
    try:  #First قم بتنفيذ البرنامج بعد المحاولة ، إذا كان تنسيق الإدخال غير صحيح ، قم بتنفيذ البرنامج بعد استثناء getopt.GetoptError:
        opts, args = getopt.getopt(argv[1:], "i:o:h", ["input", "output","help"])  # معلمات إدخال سطر الأمر
    except getopt.GetoptError:
        print("معلمة الإدخال خاطئة ، تنسيق الإدخال هو: python wavinfo.py -i voice.wav -o text1.txt ، \ nWavinfo.py هو اسم ملف البرنامج ، و voice.wav هو الملف الصوتي ، و text1.txt هو ملف .wav الملف حيث يتم حفظ البيانات ")
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):   # تعليمات الطباعة
            print("قراءة رقم قناة الملف الصوتي ، تردد أخذ العينات ، عمق أخذ العينات ، نقاط أخذ العينات")
            print("تنسيق الإدخال هو:")
            print('python wavinfo.py -i voice.wav -o text1.txt')
            print("Wavinfo.py هو اسم ملف البرنامج ، و voice.wav هو ملف الصوت ، و text1.txt هو الملف حيث يتم حفظ بيانات ملف .wav. ")
            sys.exit()
        elif opt in ("-i", "--input"):
            input = arg
            f = wave.open(input, "rb")
            # قراءة معلومات التنسيق
            # قم بإرجاع معلومات التنسيق لجميع ملفات WAV في وقت واحد ، حيث تقوم بإرجاع مجموعة: عدد القنوات ، وعدد بتات التكميم (وحدات البايت) ، وتكرار أخذ العينات ، وعدد نقاط أخذ العينات ، ونوع الضغط ، ووصف نوع الضغط. تدعم وحدة الموجة البيانات غير المضغوطة فقط ، لذلك يمكن تجاهل آخر رسالتين
            params = f.getparams()
            nchannels, sampwidth, framerate, nframes = params[:4]
            print("عدد القنوات =", nchannels, "\ n بت الكمية =", sampwidth, "\ n تردد أخذ العينات =", framerate, "\ n عدد نقاط أخذ العينات =", nframes)
        elif opt in ("-o", "--output"):
            output = arg
            params = f.getparams()
            # file = open('results_storage.txt', 'a')
            file = open(output, 'w+')
            bins = ['عدد القنوات', "بتات الكم (وحدة بايت)", "تكرار أخذ العينات", "نقاط أخذ العينات"]
            # i=0
            # حفظ في ملف النص المحلي
            params = params[:4]
            for i in range(4):
                # s = str (bins [i]). استبدل ('['، "). استبدل ('['،") + '\ t' + str (data [i]). استبدل ('['، ") .replace ('['، ") # Remove [] ، يختلف السطران حسب البيانات ، يمكنك الاختيار
                s = str(bins[i]).replace('[', ").replace('[',") + '=' + str(params[i]).replace('[', ").replace('[',")
                s = s.replace("'", ").replace(',',") + '\n'  # إزالة علامات الاقتباس الفردية ، والفواصل ، وإلحاق سطر جديد في نهاية كل سطر
                file.write(s)
            file.close()
            f.close()

if __name__ == '__main__':
    main(sys.argv)  # وظائف الاتصال
    
#python wavinfo.py -i voice.wav -o text1.txt
#python wavinfo.py -h