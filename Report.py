�
�h
`c           @   s8  d  d l  Z  d  d l Z d  d l Z d  d l m Z d Z d Z d Z d Z d Z	 d GHd	 GHd
 GHd GHd GHd
GHd GHd GHe d GHe d GHe d GHe d GHe d GHd GHe d GHe d GHd GHe j
 �  Z e  j �  Z
e j d � d Z e d � a e d � a e d � Z e e d � � Z d GHe d  � Z d! �  Z d" �  Z d# �  Z d$ �  Z d% �  Z d& �  Z d' �  Z d( �  Z e d) k r�e �  n  e d* k r�e �  n  e d+ k r�e �  n  e d, k r�e �  n  e d- k r�e �  n  e d. k re �  n  e d/ k re �  n  e d0 k r-e �  n  e �  d S(1   i����N(   t   sleeps   [1;31ms   [1;32ms   [1;33ms   [1;36ms   [1;37ms4   [1;32m              _                             _s>   [1;32m  __   ___.--'_`.                       .'_`--.___   __s?   [1;32m ( _`.'. -   'o` )                     ( 'o`   - .`.'_ )s?   [1;32m _\.'_'      _.-'                       `-._      `_`./_s?   [1;32m( \`. )    //\` report instagram         '/\    ( .'/  )s?   [1;32m \_`-'`---'\__,                        ,__//`---'`-'_/ /s>   [1;32m  \`        `-\                        /-'        '/  /s?   [1;32m   `                                               `_ / s       __  ___s$      /  |/  /___ _______      ______ _s$     / /|_/ / __ `/ ___/ | /| / / __ `/s#    / /  / / /_/ / /   | |/ |/ / /_/ /s"   /_/  /_/\__,_/_/    |__/|__/\__,_/t    s               | |    | |s               |_|\/\/|_|s                  👉👈   i   i   s
   your user:s   your password:s   target:s   sleep:s�   [1] = spam
[2] = self injury
[3] = hate speech or symbols
[4] =harsement or bulying
[5] = sale or drugs
[6] = violance
[7] = Nudity or pornography
[8] = me ( impreion)s   mode?c          C   s[  d }  i d d 6d d 6t  d 6} i t d 6d j t � d	 6d
 d 6d d
6} t j |  d | d | �} d | j k rWt j j i | j	 d d 6� d GHd j t
 � } t j | � j �  } t
| d � } | j d � d } d } xn t rSd j | � }	 i d d 6d d 6d d 6}
 t j |	 d |
 �} d j | � GHt t � | d 7} q� Wn  d  S(   Ns.   https://www.instagram.com/accounts/login/ajax/ss   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36s
   user-agentt   missings   x-csrftokent   midt   usernames&   #PWD_INSTAGRAM_BROWSER:0:1589682409:{}t   enc_passwords   {}t   queryParamst   falset
  optIntoOneTapt   headerst   datat   userIdt	   csrftokens   X-CSRFTokens
   login Trues#   https://www.instagram.com/{}/?__a=1t   logging_page_idt   _i   s*   https://www.instagram.com/users/{}/report/t    t   source_namet	   reason_idt   frx_contexts   done spam {}(   t   cookieR   t   formatt   passwordt   rt   postt   textR	   t   updatet   cookiest   targett   gett   jsont   strt   splitt   TrueR    t   sle(   t   urlR	   R
   t	   req_logint   url_idt   req_idt   user_idt   iddt   donet
   url_reportt   datast   report(    (    s   Report-Instagram-/Report.pyt   spam-   s,    

	
c          C   s[  d }  i d d 6d d 6t  d 6} i t d 6d j t � d	 6d
 d 6d d
6} t j |  d | d | �} d | j k rWt j j i | j	 d d 6� d GHd j t
 � } t j | � j �  } t
| d � } | j d � d } d } xn t rSd j | � }	 i d d 6d d 6d d 6}
 t j |	 d |
 �} d j | � GHt t � | d 7} q� Wn  d  S(   Ns.   https://www.instagram.com/accounts/login/ajax/ss   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36s
   user-agentR   s   x-csrftokenR   R   s&   #PWD_INSTAGRAM_BROWSER:0:1589682409:{}R   s   {}R   R   R   R	   R
   R   R   s   X-CSRFTokens
   login Trues#   https://www.instagram.com/{}/?__a=1R
  R   i   s*   https://www.instagram.com/users/{}/report/R   R   i   R   R   s   done self {}(   R   R   R   R   R   R   R   R	   R   R   R   R   R   R   R   R    R    R!   (   R"   R	   R
   R#   R$   R%   R&   R'   R(   R)   R*   R+   (    (    s   Report-Instagram-/Report.pyt   selfF   s,    

	
c          C   s[  d }  i d d 6d d 6t  d 6} i t d 6d j t � d	 6d
 d 6d d
6} t j |  d | d | �} d | j k rWt j j i | j	 d d 6� d GHd j t
 � } t j | � j �  } t
| d � } | j d � d } d } xn t rSd j | � }	 i d d 6d d 6d d 6}
 t j |	 d |
 �} d j | � GHt t � | d 7} q� Wn  d  S(   Ns.   https://www.instagram.com/accounts/login/ajax/ss   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36s
   user-agentR   s   x-csrftokenR   R   s&   #PWD_INSTAGRAM_BROWSER:0:1589682409:{}R   s   {}R   R   R   R	   R
   R   R   s   X-CSRFTokens
   login Trues#   https://www.instagram.com/{}/?__a=1R
  R   i   s*   https://www.instagram.com/users/{}/report/R   R   i   R   R   s   done hate {}(   R   R   R   R   R   R   R   R	   R   R   R   R   R   R   R   R    R    R!   (   R"   R	   R
   R#   R$   R%   R&   R'   R(   R)   R*   R+   (    (    s   Report-Instagram-/Report.pyt   hate`   s,    

	
c          C   s[  d }  i d d 6d d 6t  d 6} i t d 6d j t � d	 6d
 d 6d d
6} t j |  d | d | �} d | j k rWt j j i | j	 d d 6� d GHd j t
 � } t j | � j �  } t
| d � } | j d � d } d } xn t rSd j | � }	 i d d 6d d 6d d 6}
 t j |	 d |
 �} d j | � GHt t � | d 7} q� Wn  d  S(   Ns.   https://www.instagram.com/accounts/login/ajax/ss   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36s
   user-agentR   s   x-csrftokenR   R   s&   #PWD_INSTAGRAM_BROWSER:0:1589682409:{}R   s   {}R   R   R   R	   R
   R   R   s   X-CSRFTokens
   login Trues#   https://www.instagram.com/{}/?__a=1R
  R   i   s*   https://www.instagram.com/users/{}/report/R   R   i   R   R   s   done harsement {}(   R   R   R   R   R   R   R   R	   R   R   R   R   R   R   R   R    R    R!   (   R"   R	   R
   R#   R$   R%   R&   R'   R(   R)   R*   R+   (    (    s   Report-Instagram-/Report.pyt	   harsementz   s,    

	
c          C   s[  d }  i d d 6d d 6t  d 6} i t d 6d j t � d	 6d
 d 6d d
6} t j |  d | d | �} d | j k rWt j j i | j	 d d 6� d GHd j t
 � } t j | � j �  } t
| d � } | j d � d } d } xn t rSd j | � }	 i d d 6d d 6d d 6}
 t j |	 d |
 �} d j | � GHt t � | d 7} q� Wn  d  S(   Ns.   https://www.instagram.com/accounts/login/ajax/ss   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36s
   user-agentR   s   x-csrftokenR   R   s&   #PWD_INSTAGRAM_BROWSER:0:1589682409:{}R   s   {}R   R   R   R	   R
   R   R   s   X-CSRFTokens
   login Trues#   https://www.instagram.com/{}/?__a=1R
  R   i   s*   https://www.instagram.com/users/{}/report/R   R   i   R   R   s   done sale {}(   R   R   R   R   R   R   R   R	   R   R   R   R   R   R   R   R    R    R!   (   R"   R	   R
   R#   R$   R%   R&   R'   R(   R)   R*   R+   (    (    s   Report-Instagram-/Report.pyt   Ssleorpromotiondrugs�   s,    

	
c          C   s[  d }  i d d 6d d 6t  d 6} i t d 6d j t � d	 6d
 d 6d d
6} t j |  d | d | �} d | j k rWt j j i | j	 d d 6� d GHd j t
 � } t j | � j �  } t
| d � } | j d � d } d } xn t rSd j | � }	 i d d 6d d 6d d 6}
 t j |	 d |
 �} d j | � GHt t � | d 7} q� Wn  d  S(   Ns.   https://www.instagram.com/accounts/login/ajax/ss   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36s
   user-agentR   s   x-csrftokenR   R   s&   #PWD_INSTAGRAM_BROWSER:0:1589682409:{}R   s   {}R   R   R   R	   R
   R   R   s   X-CSRFTokens
   login Trues#   https://www.instagram.com/{}/?__a=1R
  R   i   s*   https://www.instagram.com/users/{}/report/R   R   i   R   R   s&   done Violence or threat of violence {}(   R   R   R   R   R   R   R   R	   R   R   R   R   R   R   R   R    R    R!   (   R"   R	   R
   R#   R$   R%   R&   R'   R(   R)   R*   R+   (    (    s   Report-Instagram-/Report.pyt   Violenceorthreatofviolence�   s,    

	
c          C   s[  d }  i d d 6d d 6t  d 6} i t d 6d j t � d	 6d
 d 6d d
6} t j |  d | d | �} d | j k rWt j j i | j	 d d 6� d GHd j t
 � } t j | � j �  } t
| d � } | j d � d } d } xn t rSd j | � }	 i d d 6d d 6d d 6}
 t j |	 d |
 �} d j | � GHt t � | d 7} q� Wn  d  S(   Ns.   https://www.instagram.com/accounts/login/ajax/ss   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36s
   user-agentR   s   x-csrftokenR   R   s&   #PWD_INSTAGRAM_BROWSER:0:1589682409:{}R   s   {}R   R   R   R	   R
   R   R   s   X-CSRFTokens
   login Trues#   https://www.instagram.com/{}/?__a=1R
  R   i   s*   https://www.instagram.com/users/{}/report/R   R   i   R   R   s   done Nudity or pornography {}(   R   R   R   R   R   R   R   R	   R   R   R   R   R   R   R   R    R    R!   (   R"   R	   R
   R#   R$   R%   R&   R'   R(   R)   R*   R+   (    (    s   Report-Instagram-/Report.pyt   Nudityorpornography�   s,    

	
c          C   sg  d }  i d d 6d d 6t  d 6} i t d 6d j t � d	 6d
 d 6d d
6} t j |  d | d | �} d | j k rWt j j i | j	 d d 6� d GHd j t
 � } t j | � j �  } t
| d � } | j d � d } d } xz t rSd j | � }	 i d d 6d d 6d d 6}
 t j |	 d |
 �} d j | � GHt t � | d 7} q� Wn d GHt �  d  S(    Ns.   https://www.instagram.com/accounts/login/ajax/ss   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36s
   user-agentR   s   x-csrftokenR   R   s&   #PWD_INSTAGRAM_BROWSER:0:1589682409:{}R   s   {}R   R   R   R	   R
   R   R   s   X-CSRFTokens
   login Trues#   https://www.instagram.com/{}/?__a=1R
  R   i   s*   https://www.instagram.com/users/{}/report/R   R   i   R   R   s
   done me {}s   login false(   R   R   R   R   R   R   R   R	   R   R   R   R   R   R   R   R    R    R!   t   exit(   R"   R	   R
   R#   R$   R%   R&   R'   R(   R)   R*   R+   (    (    s   Report-Instagram-/Report.pyt   mex�   s0    

	
t   1t   2t   3t   4t   5t   6t   7t   8(    t   requestst   uuidt   secretst   timeR    t   Rt   Gt   Yt   Ct   Wt   uuid4t   uidt   SessionR   t	   token_hexR   t   inputR   R   R   t   intR!   t   modeR,   R-   R.   R/   R0   R1   R2   R4   t   login(    (    (    s   Report-Instagram-/Report.pyt   <module>   sr   $															








