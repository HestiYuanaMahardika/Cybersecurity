import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import graphviz as graphviz
from PIL import Image
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree


# Object notation
st.sidebar.markdown("<h1 style='text-align: center; color: black;'>Welcome to Our Project</h1>", unsafe_allow_html=True)
st.sidebar.markdown("")
st.sidebar.markdown("")

from PIL import Image
image = Image.open('RB.jpg')

st.sidebar.image(image, caption='"Kebahagiaan hidupmu bergantung pada kualitas pikiranmu."')
st.sidebar.write("")

option = st.sidebar.selectbox(
    'Silakan pilih:',
    ('🏠 Home','🔍 Analisis','📝 Modeling')
)


if option == '🏠 Home' or option == '':
    st.markdown("<h2 style='text-align: center; color: green;'>ANDROID MALWARE</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("")
    st.sidebar.markdown("<h3 style='text-align: center; color:  black;'>Informasi Tambahan</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("""
            <p style=='color: black; '>Kontribusi :</p>
            <o1 style=='color: black;'>
                <li> Nama: Wa Ode Sukmasarny(Coding)</li>
                <li> Nama: Hesti Yuana(Coding)</li>
                <li> Nama: Sandra Armayanti(Konten)</li>
                <li> Nama: Nina Novita Sapitri(Konten)</li>
            </o1>
            """, unsafe_allow_html=True)
        
            
    """"""
    """"""
    """"""
    """"""
    col1, col2, col3= st.columns(3)
    with col1: 
        st.write("")
    with col2:
        st.markdown("![Alt Text](https://seclab.ge/uploads/images/2021/09/img_6154a82888a8f3-28130335-16761598.gif)")
    with col3:
        st.write("")
    """"""
    st.markdown("<div style='text-align: justify;'>Saat ini perkembangan teknologi semakin cepat berkembang, Sehingga dapat mempermudah manusia untuk mencari informasi yang ada diseluruh dunia dengan menggunakan teknologi yang tersambung internet. Dan untuk saat ini smartphone merupakan teknologi yang perkembanganya cukup cepat dalam segi jumlah pengguna. Android sendiri merupakan sistem operasi yang sangat digemari oleh pengguna teknologi saat ini. Dengan banyaknya pengguna sistem operasi Android tersebut semakin banyak pula kejahatan yang berada dalam lingkup teknologi smartphone.", unsafe_allow_html=True)
    """"""
    """"""
    st.subheader('Malicious Software')
    st.markdown("<div style='text-align: justify;'>Malicious software adalah perangkat lunak yang dirancang untuk menyerang,merusak,menonaktifkan, atau mengganggu komputer, sistem komputer, atau Jaringan. Malware mengacu pada program yang disisipkan ke dalam sebuah sistem, biasanya secara terselubung dengan maksud untuk melihat kerahasiaan korban baik berbentuk data, aplikasi, ataupun sistem oprasi.",unsafe_allow_html=True)
    """"""
    """"""
    st.subheader('Android Malware')
    st.markdown("<div style='text-align: justify;'>Android Malware adalah perangkat lunak berbahaya yang dibuat untuk menyerang sistem operasi android pada smartphone. Malware bergantung pada eksploitasi sistem operasi, tertentu dan software pada ponsel",unsafe_allow_html=True)
    st.write()
    st.write()
    """"""
    """"""
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1: 
        st.subheader("Adware")
        st.image("https://amt-it.com/wp-content/uploads/2020/01/download.png")
        

    with col2: 
       st.subheader("Spyware")
       st.image("https://amt-it.com/wp-content/uploads/2020/01/mengenal-spyware-1-1-1024x571.png")
       


    with col3: 
        st.subheader("Virus")
        st.image("https://amt-it.com/wp-content/uploads/2020/01/virus-lab-scientist-biology-cell-medical-512-1.png")
       

    with col4: 
        st.subheader("Worm")
        st.image("https://amt-it.com/wp-content/uploads/2020/01/82-512-1.png")
        st.write()

    with col5: 
        st.subheader("Trojan")
        st.image("https://amt-it.com/wp-content/uploads/2020/01/ancient-greece.png")
        st.write()

    with col6: 
        st.subheader("Ransomare")
        st.image("https://amt-it.com/wp-content/uploads/2020/01/ransomware.png")
       
    """"""
    """"""
    """"""
    st.subheader("Jenis-Jenis Malware")
    st.markdown("<div style='text-align: justify;'>A. Adware merupakan sebuah perangkat lunak yang menampilkan unduhan iklan tanpa izin dan menampilkan spanduk pada antarmuka pengguna program saat pengguna terhubung ke internet. Adware dimasukkan secara diam-diam oleh pembuat program dengan kemampuan untuk mengunduh dan menampilkan materi iklan secara otomatis tanpa di ketahui penggunanya. Adware ini umumnya berbentuk seperti iklan Pop-Up yang ada di suatu situs.", unsafe_allow_html=True)
    """"""
    st.markdown("<div style='text-align: justify;'>B. Spyware merupakan malware yang muncul sebagai aplikasi jinak, tetapi sebenarnya malware tersebut memonitori informasi rahasia pengguna seperti pesan, kontak, lokasi, dll. Spywares pribadi dapat menginstal muatan berbahaya tanpa sepengetahuan korban. Malware tersebut mengirimkan informasi korban seperti pesan teks, kontak ,dll kepada penyerang yang menginstal software tersebut pada perangkat korban", unsafe_allow_html=True)
    """"""
    st.markdown("<div style='text-align: justify;'>C. Virus merupakan Virus merupakan salah satu jenis Malware yang mempunyai kemampuan untuk memanipulasi data, menginfeksi, mengubah dan merusak sebuah program komputer perusahaan. Adapun kemampuan lain dari virus ini, yaitu dapat menggandakan diri dengan cara menyelipkan program dari kopian dari asal dirinya menjadi bagian dari program lain di komputer", unsafe_allow_html=True)
    """"""
    st.markdown("<div style='text-align: justify;'>D. Worms merupakan malware yang menyerang melalui jaringan. Misalnya, worm bluetooth menyebarkan malware melalui jaringan bluetooth dengan mengirimkan salinan malware keperangkat yang terhubung", unsafe_allow_html=True)
    """"""
    st.markdown("<div style='text-align: justify;'>E. Trojan merupakan malware yang terlihat bersifat benign. Bahkan, trojan benar benar mencuri informasi rahasia pengguna tanpa sepengetahuan pengguna. Perangkat semacam ini dapat dengan mudah mendapatkan akses ke riwayat penelusuran, pesan , kontak dll. Perangkat mencuri informasi ini tanpa persetujuan pengguna", unsafe_allow_html=True)
    """"""
    st.markdown("<div style='text-align: justify;'>F. Ransomwares merupakan malware yang mencegah pengguna mengakses data mereka diperangkatnya dengan mengunci perangkat tersebut. Hingga jumlah tebusan yang diajukan penyerang dibayarkan", unsafe_allow_html=True)
    """"""  
    """""" 
    """""" 
    st.subheader('Cara Terinfeksi dan Mencegah Malware pada Perangkat Android\n\n')
    """"""
    st.write('**A. Email Spam**\n')
    st.markdown("<div style='text-align: justify;'>Pembuat *malware* sering mencoba menipu untuk mengunduh file yang berbahaya. Salah satu bentuk penipuan berupa email dengan file terlampir yang memberi tahu bahwa email tersebut adalah tanda terima untuk pengiriman, pengembalian pajak, atau faktur untuk tiket. Sehingga membuat pengguna harus membuka lampiran tersebut untuk mendapatkan barang yang dikirimkan atau untuk mendapatkan uang.", unsafe_allow_html=True)
    """"""
    st.markdown("""
            <p style=='color: black; '>Solusi mengurangi kemungkinan perangkat terinfeksi dari email spam adalah sebagai berikut :</p>
            <o1 style=='color: black;'>
                <li> Jika tidak yakin siapa yang mengirimi email atau ada yang tidak beres diharapkan jangan dibuka</li>
                <li> Jangan pernah mengklik tautan tak terduga dalam email</li>
                <li> Jangan membuka lampiran pada email yang tidak Anda harapkan.</li>
            </o1>
            """, unsafe_allow_html=True)

    """"""
    """"""
    """"""
    st.write('**B. Perangkat Drive yang Terinfeksi**\n')
    st.markdown("<div style='text-align: justify;'>Malware dapat diinstal secara otomatis ketika menghubungkan storage device yang terinfeksi. Malware dapat menyebar dengan menginfeksi removable drive seperti USB flash drive atau hard drive eksternal.", unsafe_allow_html=True)
    st.markdown("""
            <p style=='color: black; '>Hal yang dapat dilakukan untuk menghindari jenis infeksi dari storage device sebagai berikut :</p>
            <o1 style=='color: black;'>
                <li> Berhati-hatilah terhadap perangkat USB yang tidak dimiliki.</li>
                <li> Jangan pernah mengklik tautan tak terduga dalam email</li>
                <li> Jika memasang perangkat drive yang tidak dikenal segera jalankan pemindaian keamanan.</li>
            </o1>
            """, unsafe_allow_html=True)

    """"""
    """"""
    st.write('**C. Perangkat Lunak yang Terinfeksi**\n')
    st.markdown("<div style='text-align: justify;'>Malware dapat diinstal bersamaan dengan program lain yang telah diunduh. Sehingga lebih dikenal sebagai perangkat lunak dari situs web pihak ketiga atau file yang dibagikan melalui jaringan peer-to-peer. Beberapa program juga akan menginstal perangkat lunak lain yang mungkin tidak diinginkan. Salah satu contohnya yaitu program yang menampilkan iklan tambahan saat menggunkan website tersebut.", unsafe_allow_html=True)
    """"""
    st.markdown("""
            <p style=='color: black; '>Langkah dalam menghindari pemasangan malware atau perangkat lunak yang mungkin tidak diinginkan dengan cara sebagai berikut:</p>
            <o1 style=='color: black;'>
                <li> Selalu unduh perangkat lunak dari situs web vendor resmi</li>
                <li> Pastikan membaca dengan tepat ketika akan menginstal, jangan hanya mengklik OK</li>
            </o1>
            """, unsafe_allow_html=True)

    """"""
    """"""
    st.write('**D. Halaman Website yang Diretas**\n')
    st.write('*Malware* dapat menggunakan kerentanan perangkat lunak yang diketahui untuk menginfeksi perangkat android. Kerentanan seperti lubang di perangkat android yang dapat memberikan akses malware. Salah satunya dengan cara situs web tersebut yang mungkin berbahaya atau dapat berupa situs web sah yang telah disusupi atau diretas.')
    st.write('Hal yang dapat dilakukan untuk menghindari jenis infeksi dari website yang telah diretas adalah sebagai berikut :')
    st.write('1. Sangat penting untuk selalu memperbarui semua perangkat lunak pada android yang dimiliki terutama browser web serta menghapus perangkat lunak yang tidak digunakan, termasuk ekstensi browser yang tidak digunakan.')
    st.write('2. Mengurangi kemungkinan terkena malware dengan cara dengan menggunakan browser modern, seperti google chrome atau firefox dan terus memperbaruinya.\n\n')

    """"""
    """"""
    st.subheader('Cara Menghapus Malware pada Perangkat Android\n\n')
    st.video("https://youtu.be/bNu3YT2XKds")


elif option == '🔍 Analisis':
    st.subheader('Statistik Analisis') #Menampilkan judul halaman dataframe
    st.markdown("<div style='text-align: justify;'>Statistik Analisis merupakan Teknik static analysis dilakukan tanpa menjalankan aplikasi dalam emulator atau perangkat android. Analisi statis adalah teknik untuk mengamati perilaku malware dengan menganalisa segmen code. Namun ada beberapa kelamahan static analysis yaitu ada beberapa code yang sulit dipecahkan dengan teknik ini. Keuntungan dari analisis ini adalah biayanya yang terhitung murah dan tidak memakan waktu banyak.", unsafe_allow_html=True)
    """"""
    """"""
    #Convert file into dataset
    data = pd.read_csv('train.csv',sep=";")
    #Explore first five rows in the dataset
    data.describe()
    st.write('**A. Outputs allow us to get insights about a difference between the permissions used by the malware and the benign applications**')
    fig, axs =  plt.subplots(nrows=2, sharex=True)
    pd.Series.sort_values(data[data.type==0].sum(axis=0), ascending=False)[:10].plot.bar(ax=axs[0])
    pd.Series.sort_values(data[data.type==1].sum(axis=0), ascending=False)[1:11].plot.bar(ax=axs[1],color="red")
    st.pyplot(plt)

    #Show and Hide DataFrame --> RUN
    if  st.checkbox('Show raw data'):
        st.subheader('Raw Data Permission')
        st.write(data)
        st.write('https://www.kaggle.com/competitions/microsoft-malware-prediction/rules')
        data = data.astype("int64")
        """"""
        """"""

        # Let's get the top 10 of permissions that are used for our malware samples
        st.subheader('Top 10 of Permissions That are Used for Our Malware Samples')
    
        st.write('**A. Malicious**\n') 
        tab1, tab2, tab3 = st.tabs(["🗃 Table", "📈 Line Chart","⭕ Pie Chart"])
        data1 = pd.Series.sort_values(data[data.type==1].sum(axis=0), ascending=False)[1:11] # Create malicious table
        tab1.write("Table")
        tab1.write(data1)
        tab2.write("Line Chart")
        tab2.line_chart(data1)
        tab3.write("Pie Chart")
        ability = ['Internet', 'Read Phone State', 'Acces Network State','Write External Storage', 'Acces Wifi State', 'Read SMS', 'Write SMS', 'Receive Boot Compleceted', 'Acces Coarse Location', 'Change Wifi State']
        fig = px.pie(data1, values=data1[:10], names=ability[:10])
        tab3.plotly_chart(fig)

        st.write('\n')
        st.write('\n')
    
        st.write('**B. Benign**\n')
        tab1, tab2, tab3 = st.tabs(["🗃 Table", "📈 Line Chart","⭕ Pie Chart"])
        data2 = pd.Series.sort_values(data[data.type==0].sum(axis=0), ascending=False)[:10] # Create benign table
        tab1.write("Table")
        tab1.write(data2)
        tab2.write("Line Chart")
        tab2.line_chart(data2)
        tab3.write("Pie Chart")
        ability = ['Internet', 'Read Phone State', 'Acces Network State','Write External Storage', 'Acces Wifi State', 'Read SMS', 'Write SMS', 'Receive Boot Compleceted', 'Acces Coarse Location', 'Change Wifi State']
        fig = px.pie(data2, values=data2[:10], names=ability[:10])
        tab3.plotly_chart(fig)

elif option == '📝 Modeling':
    st.markdown("<h1 style='text-align: center; color: green;'>Modeling</h1>", unsafe_allow_html=True)
    st.subheader(" ")
    # Create a graphlib graph object
    """"""
    graph = graphviz.Digraph()
    graph.edge('Malware analysis', 'Feature extraction')
    graph.edge('Malware analysis', 'Classification')
    graph.edge('Feature extraction', 'Static analysis')
    graph.edge('Feature extraction', 'Dynamic analysis')
    graph.edge('Classification', 'Decision Tree')
    graph.edge('Classification', 'Naive Bayes')
    st.graphviz_chart(graph)
    """"""
   
    col1, col2, col3= st.columns(3)
    with col1: 
        st.write("")
    with col2:
        st.write("**Gbr.  Analisis Malware Taxonomy**")
    with col3:
        st.write("")
    """"""
    """"""
    # Convert file into dataset
    data = pd.read_csv('train.csv',sep=";")
    st.write('**Tabel. Raw Data Permission**')
    
    # Explore first five rows in the dataset
    data.describe()
    st.write(data)
    data = data.astype("int64")

    st.subheader('**A. Naive Bayes**')
    st.write('Tabel Modeling Naive Bayes')
    X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, 1:330], data['type'], test_size=0.20, random_state=42)
    # Naive bayes algorithm
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    # Read the csv test file
    pred = gnb.predict(X_test)
    # Accuracy
    accuracy = accuracy_score(pred, y_test)
    st.write(accuracy)
    st.text('Naive Bayes:\n ' + classification_report(pred, y_test, labels=None))
    """"""
    """"""
    st.subheader('**C. Decision Tree**')
    st.write('Tabel Modeling Decision Tree')
    # Decision tree algorithm
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    # Read the csv test file
    pred = clf.predict(X_test)
    # Accuracy
    accuracy = accuracy_score(pred, y_test)
    st.write(accuracy)
    st.text('Decision Tree:\n ' + classification_report(pred, y_test, labels=None))
    """"""
    """"""

    st.subheader("Kesimpulan")
    st.markdown("<div style='text-align: justify;'>Berdasarkan pengujian dan analisis terhadap malware android yang telah dilakukan maka dapat disimpulkan bahwa pendeteksian keberadaan malware dapat menggunakan algoritma decision tree dan naive bayes dimana nilai akurasinya lebih besar dibandingkan yang lainnya.", unsafe_allow_html=True)

st.sidebar.markdown("")
st.sidebar.markdown("")
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("📧 Email", "📞 Home phone", "📱 Mobile phone")
)

st.sidebar.markdown("")
add_selectbox = st.sidebar.selectbox(
    "🌐 Select your language:",
    ("Indonesian (🇮🇩)", "English (🇺🇸)")
)





