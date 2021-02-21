from django.shortcuts import render

def home(request):
    konten = {  'judul' : 'SMK Islam Al-Fikri',
                'deskripsi_sekolah'   : 'Sekolah islam berbasis teknologi yang dipadukan dengan pengelolaan bisnis mumpuni',
                'deskripsi_rpl' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat',
                'deskripsi_bisnis' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
                'deskripsi_lab' : 'Peralatan Laboratorium yang canggih, sebagai fasilitas siswa untuk melakukan berbagai eksperimen',
                'deskripsi_wifi' : 'Internet yang cepat hingga 20Mbps tersedia gratis untuk membantu proses belajar-mengajar dan hiburan siswa',
                'deskripsi_lapangan' : 'Lapangan yang luas untuk kegiatan olahraga juga kegiatan lainnya, sebagai fasilitas siswa baik dalam belajar maupun bermain',
                'deskripsi_ekskul' : 'Kegiatan ekstra agar siswa lebih aktif dalam mengembangkan minatnya serta bekerja sama mencapai prestasi lebih'
             }
    return render(request, 'home.html', konten)
