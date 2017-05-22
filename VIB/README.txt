
Software yang diperlukan:
Python dengan Numpy dan ASE

File2 yang harus diedit:

- COMMON.py
- TEMPL_1
- TEMPL_2

Step 1
------

gen_pwinput.py

gen_pwinput.py untuk menghasilkan file2 input PWSCF dengan struktur yang
sudah digeser untuk perhitungan Hessian.

File TEMPL_1 dan TEMPL_2: template untuk input PWSCF. Masukkan
sesuai dengan sistem yang akan dihitung, yang penting ada opsi

File COMMON.py: parameter2 untuk perhitungan Hessian.

calculation = 'scf'
tprnfor = .true.

File struktur geometri dapat diberikan di file STRUCT.xyz
(dalam angstrom).
Struktur yg lain juga dapat digunakan, namun file gen_pwinput.py harus diedit.

Jalankan:

  python gen_pwinput.py

File2 input PWSCF yang diperlukan akan dihasilkan.
Setelah itu PWSCF dapat dijalankan seperti biasanya.
gen_pwinput.py juga akan membuat bash script untuk command
PWSCF. Silakan diedit untuk MPI.


Langkah 2
---------

Setelah seluruh job PWSCF selesai, mode vibrasi dapat dihitung
dengan menggunakan script calc_vib.py.

  python calc_vib.py

Script ini juga akan menghasilkan file VIB.xyz yang dapat divisualisasi
dengan Jmol untuk visualisas mode vibrasi.
