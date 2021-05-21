%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-p
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1411:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/natbib.tar.xz
Source1412:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/natbib.doc.tar.xz
Source1487:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multibib.tar.xz
Source1488:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multibib.doc.tar.xz
Source1493:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/munich.tar.xz
Source1494:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/munich.doc.tar.xz
Source1495:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nar.tar.xz
Source1496:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nmbib.tar.xz
Source1497:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nmbib.doc.tar.xz
Source1970:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newpx.tar.xz
Source1971:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newpx.doc.tar.xz
Source1972:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newtx.tar.xz
Source1973:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newtx.doc.tar.xz
Source1974:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newtxsf.tar.xz
Source1975:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newtxsf.doc.tar.xz
Source1976:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newtxtt.tar.xz
Source1977:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newtxtt.doc.tar.xz
Source1978:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nkarta.tar.xz
Source1979:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nkarta.doc.tar.xz
Source2138:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ncntrsbk.tar.xz
Source2312:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/navigator.tar.xz
Source2313:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/navigator.doc.tar.xz
Source2352:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multido.tar.xz
Source2353:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multido.doc.tar.xz
Source2387:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ncctools.tar.xz
Source2388:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ncctools.doc.tar.xz
Source2574:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mongolian-babel.tar.xz
Source2575:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mongolian-babel.doc.tar.xz
Source2577:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/montex.tar.xz
Source2578:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/montex.doc.tar.xz
Source2579:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mpman-ru.doc.tar.xz
Source2700:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nevelok.tar.xz
Source2701:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nevelok.doc.tar.xz
Source2930:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nanumtype1.tar.xz
Source2931:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nanumtype1.doc.tar.xz
Source2959:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mwcls.tar.xz
Source2960:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mwcls.doc.tar.xz
Source3062:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ms.tar.xz
Source3063:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ms.doc.tar.xz
Source3208:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modiagram.tar.xz
Source3209:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modiagram.doc.tar.xz
Source3210:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/neuralnetwork.tar.xz
Source3211:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/neuralnetwork.doc.tar.xz
Source4650:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moderncv.tar.xz
Source4651:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moderncv.doc.tar.xz
Source4652:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moderntimeline.tar.xz
Source4653:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moderntimeline.doc.tar.xz
Source4655:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modref.tar.xz
Source4656:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modref.doc.tar.xz
Source4658:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modroman.tar.xz
Source4659:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modroman.doc.tar.xz
Source4661:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/monofill.tar.xz
Source4662:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/monofill.doc.tar.xz
Source4664:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moreenum.tar.xz
Source4665:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moreenum.doc.tar.xz
Source4666:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/morefloats.tar.xz
Source4667:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/morefloats.doc.tar.xz
Source4669:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/morehype.tar.xz
Source4670:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/morehype.doc.tar.xz
Source4672:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moresize.tar.xz
Source4673:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moresize.doc.tar.xz
Source4675:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moreverb.tar.xz
Source4676:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moreverb.doc.tar.xz
Source4678:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/morewrites.tar.xz
Source4679:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/morewrites.doc.tar.xz
Source4683:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mparhack.tar.xz
Source4684:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mparhack.doc.tar.xz
Source4686:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/msc.tar.xz
Source4687:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/msc.doc.tar.xz
Source4688:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/msg.tar.xz
Source4689:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/msg.doc.tar.xz
Source4691:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mslapa.tar.xz
Source4692:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mslapa.doc.tar.xz
Source4693:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mtgreek.tar.xz
Source4694:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mtgreek.doc.tar.xz
Source4696:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multenum.tar.xz
Source4697:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multenum.doc.tar.xz
Source4698:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multiaudience.tar.xz
Source4699:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multiaudience.doc.tar.xz
Source4701:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multibbl.tar.xz
Source4702:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multibbl.doc.tar.xz
Source4704:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multicap.tar.xz
Source4705:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multicap.doc.tar.xz
Source4707:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multienv.tar.xz
Source4708:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multienv.doc.tar.xz
Source4710:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multiexpand.tar.xz
Source4711:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multiexpand.doc.tar.xz
Source4713:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multirow.tar.xz
Source4714:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multirow.doc.tar.xz
Source4715:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mversion.tar.xz
Source4716:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mversion.doc.tar.xz
Source4718:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mwe.tar.xz
Source4719:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mwe.doc.tar.xz
Source4721:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mweights.tar.xz
Source4722:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mweights.doc.tar.xz
Source4723:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mycv.tar.xz
Source4724:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mycv.doc.tar.xz
Source4726:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mylatexformat.tar.xz
Source4727:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mylatexformat.doc.tar.xz
Source4729:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nag.tar.xz
Source4730:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nag.doc.tar.xz
Source4732:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nameauth.tar.xz
Source4733:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nameauth.doc.tar.xz
Source4735:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/namespc.tar.xz
Source4736:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/namespc.doc.tar.xz
Source4738:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ncclatex.tar.xz
Source4739:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ncclatex.doc.tar.xz
Source4740:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/needspace.tar.xz
Source4741:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/needspace.doc.tar.xz
Source4743:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nestquot.tar.xz
Source4744:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newcommand.doc.tar.xz
Source4745:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newenviron.tar.xz
Source4746:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newenviron.doc.tar.xz
Source4747:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newfile.tar.xz
Source4748:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newfile.doc.tar.xz
Source4750:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newlfm.tar.xz
Source4751:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newlfm.doc.tar.xz
Source4753:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newspaper.tar.xz
Source4754:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newspaper.doc.tar.xz
Source4756:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newunicodechar.tar.xz
Source4757:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newunicodechar.doc.tar.xz
Source4759:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newvbtm.tar.xz
Source4760:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newvbtm.doc.tar.xz
Source4762:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newverbs.tar.xz
Source4763:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newverbs.doc.tar.xz
Source4765:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nextpage.tar.xz
Source4766:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nfssext-cfr.tar.xz
Source4767:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nfssext-cfr.doc.tar.xz
Source4768:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nicefilelist.tar.xz
Source4769:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nicefilelist.doc.tar.xz
Source4771:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/niceframe.tar.xz
Source4772:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/niceframe.doc.tar.xz
Source4774:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nicetext.tar.xz
Source4775:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nicetext.doc.tar.xz
Source4777:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nlctdoc.tar.xz
Source4778:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nlctdoc.doc.tar.xz
Source5873:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multiobjective.tar.xz
Source5874:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multiobjective.doc.tar.xz
Source5876:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/natded.tar.xz
Source5877:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/natded.doc.tar.xz
Source5878:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nath.tar.xz
Source5879:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nath.doc.tar.xz
Source5991:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mp3d.tar.xz
Source5992:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mp3d.doc.tar.xz
Source5993:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mpcolornames.tar.xz
Source5994:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mpcolornames.doc.tar.xz
Source5996:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mpattern.tar.xz
Source5997:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mpattern.doc.tar.xz
Source5998:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mpgraphics.tar.xz
Source5999:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mpgraphics.doc.tar.xz
Source6044:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musixguit.tar.xz
Source6045:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musixguit.doc.tar.xz
Source6049:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musixtex-fonts.tar.xz
Source6050:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musixtex-fonts.doc.tar.xz
Source6068:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mxedruli.tar.xz
Source6069:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mxedruli.doc.tar.xz
Source6097:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newsletr.tar.xz
Source6098:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/newsletr.doc.tar.xz
Source6442:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/msu-thesis.tar.xz
Source6443:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/msu-thesis.doc.tar.xz
Source6444:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mugsthesis.tar.xz
Source6445:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mugsthesis.doc.tar.xz
Source6447:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musuos.tar.xz
Source6448:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musuos.doc.tar.xz
Source6450:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/muthesis.tar.xz
Source6451:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/muthesis.doc.tar.xz
Source6452:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nature.tar.xz
Source6453:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nature.doc.tar.xz
Source6454:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nddiss.tar.xz
Source6455:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nddiss.doc.tar.xz
Source6457:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ndsu-thesis.tar.xz
Source6458:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ndsu-thesis.doc.tar.xz
Source6459:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nih.tar.xz
Source6460:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nih.doc.tar.xz
Source6700:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mychemistry.tar.xz
Source6701:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mychemistry.doc.tar.xz
Source7440:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moodle.tar.xz
Source7441:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/moodle.doc.tar.xz
Source7443:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mparrows.tar.xz
Source7444:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mparrows.doc.tar.xz
Source7445:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multidef.tar.xz
Source7446:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multidef.doc.tar.xz
Source7448:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mynsfc.tar.xz
Source7449:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mynsfc.doc.tar.xz
Source7451:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nihbiosketch.tar.xz
Source7452:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nihbiosketch.doc.tar.xz
Source7453:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nimbus15.tar.xz
Source7454:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nimbus15.doc.tar.xz
Source7854:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modular.tar.xz
Source7855:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modular.doc.tar.xz
Source7856:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/montserrat.tar.xz
Source7857:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/montserrat.doc.tar.xz
Source7858:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mpostinl.tar.xz
Source7859:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mpostinl.doc.tar.xz
Source7860:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mucproc.tar.xz
Source7861:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mucproc.doc.tar.xz
Source7862:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multilang.tar.xz
Source7863:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multilang.doc.tar.xz
Source7864:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musicography.tar.xz
Source7865:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musicography.doc.tar.xz
Source7866:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/na-box.tar.xz
Source7867:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/na-box.doc.tar.xz
Source7868:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/na-position.tar.xz
Source7869:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/na-position.doc.tar.xz
Source7870:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/navydocs.tar.xz
Source7871:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/navydocs.doc.tar.xz
Source7872:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/niceframe-type1.tar.xz
Source7873:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/niceframe-type1.doc.tar.xz
Source8040:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modulus.doc.tar.xz
Source8041:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modulus.tar.xz
Source8228:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modernposter.tar.xz
Source8229:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/modernposter.doc.tar.xz
Source8232:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/morisawa.tar.xz
Source8233:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/morisawa.doc.tar.xz
Source8234:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mptrees.tar.xz
Source8235:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mptrees.doc.tar.xz
Source8236:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musikui.tar.xz
Source8237:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musikui.doc.tar.xz
Source8238:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nicematrix.tar.xz
Source8239:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nicematrix.doc.tar.xz
Source8240:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nidanfloat.tar.xz
Source8241:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/nidanfloat.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-natbib
Provides:       tex-natbib = %{tl_version}
License:        LPPL
Summary:        Flexible bibliography support
Version:        svn20668.8.31b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bibentry.sty) = %{tl_version}, tex(natbib.sty) = %{tl_version}

%description -n texlive-natbib
The bundle provides a package that implements both author-year
and numbered references, as well as much detailed of support
for other bibliography use. Also Provided are versions of the
standard BibTeX styles that are compatible with natbib--
plainnat, unsrtnat, abbrnat. The bibliography styles produced
by custom-bib are designed from the start to be compatible with
natbib.

%package -n texlive-natbib-doc
Summary:        Documentation for natbib
Version:        svn20668.8.31b

Provides:       tex-natbib-doc
AutoReqProv:    No

%description -n texlive-natbib-doc
Documentation for natbib

%package -n texlive-multibib
Provides:       tex-multibib = %{tl_version}
License:        LPPL
Summary:        Multiple bibliographies within one document
Version:        svn15878.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(multibib.sty) = %{tl_version}

%description -n texlive-multibib
The package the creation of references to multiple
bibliographies within one document. It thus provides
complementary functionality to packages like bibunits and
chapterbib, which allow the creation of one bibliography for
multiple, but different parts of the document. Multibib is
compatible with inlinebib, natbib, and koma-script.

%package -n texlive-multibib-doc
Summary:        Documentation for multibib
Version:        svn15878.1.4

Provides:       tex-multibib-doc
AutoReqProv:    No

%description -n texlive-multibib-doc
Documentation for multibib

%package -n texlive-munich
Provides:       tex-munich = %{tl_version}
License:        LPPL
Summary:        An alternative authordate bibliography style
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-munich
The Munich BibTeX style is produced with custom-bib, as a
German (and, more generally, Continental European) alternative
to such author-date styles as harvard and oxford.

%package -n texlive-munich-doc
Summary:        Documentation for munich
Version:        svn15878.0

Provides:       tex-munich-doc
AutoReqProv:    No

%description -n texlive-munich-doc
Documentation for munich

%package -n texlive-nar
Provides:       tex-nar = %{tl_version}
License:        Bibtex
Summary:        BibTeX style for Nucleic Acid Research
Version:        svn38100.3.19

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-nar
This BibTeX bibliography style is for the journal Nucleic Acid
Research. It was adapted from the standard unsrt.bst style
file.

%package -n texlive-nmbib
Provides:       tex-nmbib = %{tl_version}
License:        LPPL 1.3
Summary:        Multiple versions of a bibliography, with different sort orders
Version:        svn37984.1.04

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(natbib.sty)
Provides:       tex(nmbib.sty) = %{tl_version}

%description -n texlive-nmbib
This package is a rewrite of the multibibliography package
providing multiple bibliographies with different sorting. The
new version offers a number of citation commands, streamlines
the creation of bibliographies, ensures compatibility with the
natbib package, and provides other improvements.

%package -n texlive-nmbib-doc
Summary:        Documentation for nmbib
Version:        svn37984.1.04

Provides:       tex-nmbib-doc
AutoReqProv:    No

%description -n texlive-nmbib-doc
Documentation for nmbib

%package -n texlive-newpx
Provides:       tex-newpx = %{tl_version}
License:        LPPL
Summary:        Alternative uses of the PX fonts, with improved metrics
Version:        svn45075
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(amsmath.sty)
Requires:       tex(xkeyval.sty), tex(binhex.tex), tex(fontaxes.sty), tex(fontenc.sty)
Requires:       tex(textcomp.sty)
Provides:       tex(ecsups.enc) = %{tl_version}, tex(ot1sups.enc) = %{tl_version}
Provides:       tex(texnansxsups.enc) = %{tl_version}, tex(tgpdiff.enc) = %{tl_version}
Provides:       tex(newpx.map) = %{tl_version}, tex(newpxtext.map) = %{tl_version}
Provides:       tex(TeXGyrePagellaX-Bold.otf) = %{tl_version}
Provides:       tex(TeXGyrePagellaX-BoldItalic.otf) = %{tl_version}
Provides:       tex(TeXGyrePagellaX-Italic.otf) = %{tl_version}
Provides:       tex(TeXGyrePagellaX-Regular.otf) = %{tl_version}
Provides:       tex(zpl-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-lf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-lf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-lf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-lf-t1.tfm) = %{tl_version}, tex(zpl-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-osf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-osf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-osf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-lf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-lf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-lf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-th-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-th-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-osf-th-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-th-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-th-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-th-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-lf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-lf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-lf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-osf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-osf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-osf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-scl-t1.tfm) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(zplb-x.tfm) = %{tl_version}, tex(zplbexa.tfm) = %{tl_version}
Provides:       tex(zplbexx.tfm) = %{tl_version}, tex(zplbmi.tfm) = %{tl_version}
Provides:       tex(zplbmi1.tfm) = %{tl_version}, tex(zplbmia.tfm) = %{tl_version}
Provides:       tex(zplbsy.tfm) = %{tl_version}, tex(zplbsyc.tfm) = %{tl_version}
Provides:       tex(zplbsym.tfm) = %{tl_version}, tex(zplexa.tfm) = %{tl_version}
Provides:       tex(zplexx.tfm) = %{tl_version}, tex(zplmi.tfm) = %{tl_version}
Provides:       tex(zplmi1.tfm) = %{tl_version}, tex(zplmia.tfm) = %{tl_version}
Provides:       tex(zplr-x.tfm) = %{tl_version}, tex(zplsups-Bold-ly1.tfm) = %{tl_version}
Provides:       tex(zplsups-Bold-ot1.tfm) = %{tl_version}
Provides:       tex(zplsups-Bold-t1.tfm) = %{tl_version}
Provides:       tex(zplsups-BoldItalic-ly1.tfm) = %{tl_version}
Provides:       tex(zplsups-BoldItalic-ot1.tfm) = %{tl_version}
Provides:       tex(zplsups-BoldItalic-t1.tfm) = %{tl_version}
Provides:       tex(zplsups-Italic-ly1.tfm) = %{tl_version}
Provides:       tex(zplsups-Italic-ot1.tfm) = %{tl_version}
Provides:       tex(zplsups-Italic-t1.tfm) = %{tl_version}
Provides:       tex(zplsups-Regular-ly1.tfm) = %{tl_version}
Provides:       tex(zplsups-Regular-ot1.tfm) = %{tl_version}
Provides:       tex(zplsups-Regular-t1.tfm) = %{tl_version}
Provides:       tex(zplsy.tfm) = %{tl_version}, tex(zplsyc.tfm) = %{tl_version}
Provides:       tex(zplsym.tfm) = %{tl_version}, tex(zplb.pfb) = %{tl_version}
Provides:       tex(zplbi.pfb) = %{tl_version}, tex(zplr.pfb) = %{tl_version}
Provides:       tex(zplri.pfb) = %{tl_version}, tex(zplx-bold.pfb) = %{tl_version}
Provides:       tex(zplx-regular.pfb) = %{tl_version}, tex(zpl-Bold-lf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Bold-lf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Bold-lf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-Bold-osf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Bold-osf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Bold-osf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Bold-tlf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Bold-tosf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-lf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-osf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tlf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-BoldItalic-tosf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-lf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-lf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-lf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-osf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-osf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-osf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-tlf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Italic-tosf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-lf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-lf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-lf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-osf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-osf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-osf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-tlf-scl-t1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-scl-ly1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-scl-ot1.vf) = %{tl_version}
Provides:       tex(zpl-Regular-tosf-scl-t1.vf) = %{tl_version}
Provides:       tex(zplbexa.vf) = %{tl_version}, tex(zplbexx.vf) = %{tl_version}
Provides:       tex(zplbmi.vf) = %{tl_version}, tex(zplbmi1.vf) = %{tl_version}
Provides:       tex(zplbmia.vf) = %{tl_version}, tex(zplbsy.vf) = %{tl_version}
Provides:       tex(zplbsyc.vf) = %{tl_version}, tex(zplbsym.vf) = %{tl_version}
Provides:       tex(zplexa.vf) = %{tl_version}, tex(zplexx.vf) = %{tl_version}
Provides:       tex(zplmi.vf) = %{tl_version}, tex(zplmi1.vf) = %{tl_version}
Provides:       tex(zplmia.vf) = %{tl_version}, tex(zplsy.vf) = %{tl_version}
Provides:       tex(zplsyc.vf) = %{tl_version}, tex(zplsym.vf) = %{tl_version}
Provides:       tex(ly1npxtt.fd) = %{tl_version}, tex(ly1zpllf.fd) = %{tl_version}
Provides:       tex(ly1zplosf.fd) = %{tl_version}, tex(ly1zplsups.fd) = %{tl_version}
Provides:       tex(ly1zpltlf.fd) = %{tl_version}, tex(ly1zpltosf.fd) = %{tl_version}
Provides:       tex(newpxmath.sty) = %{tl_version}, tex(newpxtext.sty) = %{tl_version}
Provides:       tex(omlnpxmi.fd) = %{tl_version}, tex(omsnpxsy.fd) = %{tl_version}
Provides:       tex(ot1npxtt.fd) = %{tl_version}, tex(ot1zpllf.fd) = %{tl_version}
Provides:       tex(ot1zplosf.fd) = %{tl_version}, tex(ot1zplsups.fd) = %{tl_version}
Provides:       tex(ot1zpltlf.fd) = %{tl_version}, tex(ot1zpltosf.fd) = %{tl_version}
Provides:       tex(t1npxtt.fd) = %{tl_version}, tex(t1zpllf.fd) = %{tl_version}
Provides:       tex(t1zplosf.fd) = %{tl_version}, tex(t1zplsups.fd) = %{tl_version}
Provides:       tex(t1zpltlf.fd) = %{tl_version}, tex(t1zpltosf.fd) = %{tl_version}
Provides:       tex(ts1npxtt.fd) = %{tl_version}, tex(ts1zpllf.fd) = %{tl_version}
Provides:       tex(ts1zplosf.fd) = %{tl_version}, tex(ts1zpltlf.fd) = %{tl_version}
Provides:       tex(ts1zpltosf.fd) = %{tl_version}, tex(unpxexa.fd) = %{tl_version}
Provides:       tex(unpxmia.fd) = %{tl_version}, tex(unpxss.fd) = %{tl_version}
Provides:       tex(unpxsyc.fd) = %{tl_version}, tex(unpxsym.fd) = %{tl_version}
Provides:       tex(unpxtt.fd) = %{tl_version}

%description -n texlive-newpx
This package, initially based on pxfonts, provides many fixes
and enhancements to that package, and splits it in two parts
(newpxtext and newpxmath) which may be run independently of one
another. It provides scaling, improved metrics, and other
options. For proper operation, the packages require that the
packages newtxmath, pxfonts, and TeXGyrePagella be installed
and their map files enabled.

%package -n texlive-newpx-doc
Summary:        Documentation for newpx
Version:        svn45075
Provides:       tex-newpx-doc
AutoReqProv:    No

%description -n texlive-newpx-doc
Documentation for newpx

%package -n texlive-newtx
Provides:       tex-newtx = %{tl_version}
License:        LPPL 1.3
Summary:        Alternative uses of the TX fonts, with improved metrics
Version:        svn47889
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, texlive-boondox
Requires:       tex(amsmath.sty), tex(ifxetex.sty), tex(ifluatex.sty), tex(xkeyval.sty)
Requires:       tex(binhex.tex), tex(fontaxes.sty), tex(fontenc.sty), tex(textcomp.sty)
Provides:       tex(alt-mn-greek.enc) = %{tl_version}, tex(libcaps.enc) = %{tl_version}
Provides:       tex(libertinealt.enc) = %{tl_version}, tex(ntx-ec-lf-sc.enc) = %{tl_version}
Provides:       tex(ntx-ec-lf.enc) = %{tl_version}, tex(ntx-ec-osf-sc.enc) = %{tl_version}
Provides:       tex(ntx-ec-osf.enc) = %{tl_version}, tex(ntx-ec-tlf-sc.enc) = %{tl_version}
Provides:       tex(ntx-ec-tlf.enc) = %{tl_version}, tex(ntx-ec-tosf-sc.enc) = %{tl_version}
Provides:       tex(ntx-ec-tosf.enc) = %{tl_version}, tex(ntx-ecth-lf.enc) = %{tl_version}
Provides:       tex(ntx-ecth-osf.enc) = %{tl_version}, tex(ntx-ecth-tlf.enc) = %{tl_version}
Provides:       tex(ntx-ecth-tosf.enc) = %{tl_version}, tex(ntx-ly1-sc.enc) = %{tl_version}
Provides:       tex(ntx-ot1-lf-sc.enc) = %{tl_version}, tex(ntx-ot1-lf.enc) = %{tl_version}
Provides:       tex(ntx-ot1-osf-sc.enc) = %{tl_version}, tex(ntx-ot1-osf.enc) = %{tl_version}
Provides:       tex(ntx-ot1-sc.enc) = %{tl_version}, tex(ntx-ot1-th-osf.enc) = %{tl_version}
Provides:       tex(ntx-ot1-th-tlf.enc) = %{tl_version}, tex(ntx-ot1-tlf-sc.enc) = %{tl_version}
Provides:       tex(ntx-ot1-tlf.enc) = %{tl_version}, tex(ntx-ot1-tosf-sc.enc) = %{tl_version}
Provides:       tex(ntx-ot1-tosf.enc) = %{tl_version}, tex(ntx-t1-sc.enc) = %{tl_version}
Provides:       tex(ntx-texnansi-lf-sc.enc) = %{tl_version}
Provides:       tex(ntx-texnansi-lf.enc) = %{tl_version}
Provides:       tex(ntx-texnansi-osf-sc.enc) = %{tl_version}
Provides:       tex(ntx-texnansi-osf.enc) = %{tl_version}
Provides:       tex(ntx-texnansi-th-osf.enc) = %{tl_version}
Provides:       tex(ntx-texnansi-th-tlf.enc) = %{tl_version}
Provides:       tex(ntx-texnansi-tlf-sc.enc) = %{tl_version}
Provides:       tex(ntx-texnansi-tlf.enc) = %{tl_version}
Provides:       tex(ntx-texnansi-tosf-sc.enc) = %{tl_version}
Provides:       tex(ntx-texnansi-tosf.enc) = %{tl_version}
Provides:       tex(ntxmiaalt.enc) = %{tl_version}, tex(newtx.map) = %{tl_version}
Provides:       tex(zmn.map) = %{tl_version}, tex(Libertine-nu.tfm) = %{tl_version}
Provides:       tex(LibertineI-5nu.tfm) = %{tl_version}, tex(LibertineI-7nu.tfm) = %{tl_version}
Provides:       tex(LibertineI-nu.tfm) = %{tl_version}, tex(LibertineTheta-Regular.tfm) = %{tl_version}
Provides:       tex(LibertineZ-nu.tfm) = %{tl_version}, tex(LibertineZI-5nu.tfm) = %{tl_version}
Provides:       tex(LibertineZI-7nu.tfm) = %{tl_version}
Provides:       tex(LibertineZI-nu.tfm) = %{tl_version}, tex(MinLibBol-ly1.tfm) = %{tl_version}
Provides:       tex(MinLibBol-ot1.tfm) = %{tl_version}, tex(MinLibBol-t1.tfm) = %{tl_version}
Provides:       tex(MinLibBolIta-ly1.tfm) = %{tl_version}
Provides:       tex(MinLibBolIta-ot1.tfm) = %{tl_version}
Provides:       tex(MinLibBolIta-t1.tfm) = %{tl_version}
Provides:       tex(MinLibIta-ly1.tfm) = %{tl_version}, tex(MinLibIta-ot1.tfm) = %{tl_version}
Provides:       tex(MinLibIta-t1.tfm) = %{tl_version}, tex(MinLibReg-ly1.tfm) = %{tl_version}
Provides:       tex(MinLibReg-ot1.tfm) = %{tl_version}, tex(MinLibReg-t1.tfm) = %{tl_version}
Provides:       tex(fxlri-5alt.tfm) = %{tl_version}, tex(fxlri-5letters.tfm) = %{tl_version}
Provides:       tex(fxlri-7alt.tfm) = %{tl_version}, tex(fxlri-7letters.tfm) = %{tl_version}
Provides:       tex(fxlzi-5alt.tfm) = %{tl_version}, tex(fxlzi-5letters.tfm) = %{tl_version}
Provides:       tex(fxlzi-7alt.tfm) = %{tl_version}, tex(fxlzi-7letters.tfm) = %{tl_version}
Provides:       tex(fxlzi-jv.tfm) = %{tl_version}, tex(fxlzi-jv5.tfm) = %{tl_version}
Provides:       tex(fxlzi-jv7.tfm) = %{tl_version}, tex(ntx-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-lf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-lf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-lf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-lf-t1.tfm) = %{tl_version}, tex(ntx-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-osf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-osf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-osf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tlf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tlf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tlf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tosf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tosf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tosf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-lf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-lf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-lf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-osf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-osf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-osf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tlf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tlf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tlf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tosf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tosf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tosf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-lf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-lf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-lf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-th-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-th-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-osf-th-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-th-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-th-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tlf-th-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tosf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tosf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tosf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-lf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-lf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-lf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-osf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-osf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-osf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tlf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tlf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tlf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tosf-scl-ly1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tosf-scl-ot1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tosf-scl-t1.tfm) = %{tl_version}
Provides:       tex(ntx-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(ntxbexa.tfm) = %{tl_version}, tex(ntxbexb.tfm) = %{tl_version}
Provides:       tex(ntxbexmods.tfm) = %{tl_version}, tex(ntxbexx.tfm) = %{tl_version}
Provides:       tex(ntxbmi.tfm) = %{tl_version}, tex(ntxbmi1.tfm) = %{tl_version}
Provides:       tex(ntxbmi15.tfm) = %{tl_version}, tex(ntxbmi17.tfm) = %{tl_version}
Provides:       tex(ntxbmi1x.tfm) = %{tl_version}, tex(ntxbmi5.tfm) = %{tl_version}
Provides:       tex(ntxbmi7.tfm) = %{tl_version}, tex(ntxbmia.tfm) = %{tl_version}
Provides:       tex(ntxbmial1.tfm) = %{tl_version}, tex(ntxbmials.tfm) = %{tl_version}
Provides:       tex(ntxbsy.tfm) = %{tl_version}, tex(ntxbsy5.tfm) = %{tl_version}
Provides:       tex(ntxbsy7.tfm) = %{tl_version}, tex(ntxbsyc.tfm) = %{tl_version}
Provides:       tex(ntxbsym.tfm) = %{tl_version}, tex(ntxexa.tfm) = %{tl_version}
Provides:       tex(ntxexb.tfm) = %{tl_version}, tex(ntxexmods.tfm) = %{tl_version}
Provides:       tex(ntxexx.tfm) = %{tl_version}, tex(ntxmi.tfm) = %{tl_version}
Provides:       tex(ntxmi1.tfm) = %{tl_version}, tex(ntxmi15.tfm) = %{tl_version}
Provides:       tex(ntxmi17.tfm) = %{tl_version}, tex(ntxmi5.tfm) = %{tl_version}
Provides:       tex(ntxmi7.tfm) = %{tl_version}, tex(ntxmia.tfm) = %{tl_version}
Provides:       tex(ntxsups-Bold-ly1.tfm) = %{tl_version}
Provides:       tex(ntxsups-Bold-ot1.tfm) = %{tl_version}
Provides:       tex(ntxsups-Bold-t1.tfm) = %{tl_version}
Provides:       tex(ntxsups-Bold.tfm) = %{tl_version}, tex(ntxsups-BoldItalic-ly1.tfm) = %{tl_version}
Provides:       tex(ntxsups-BoldItalic-ot1.tfm) = %{tl_version}
Provides:       tex(ntxsups-BoldItalic-t1.tfm) = %{tl_version}
Provides:       tex(ntxsups-BoldItalic.tfm) = %{tl_version}
Provides:       tex(ntxsups-Italic-ly1.tfm) = %{tl_version}
Provides:       tex(ntxsups-Italic-ot1.tfm) = %{tl_version}
Provides:       tex(ntxsups-Italic-t1.tfm) = %{tl_version}
Provides:       tex(ntxsups-Italic.tfm) = %{tl_version}, tex(ntxsups-Regular-ly1.tfm) = %{tl_version}
Provides:       tex(ntxsups-Regular-ot1.tfm) = %{tl_version}
Provides:       tex(ntxsups-Regular-t1.tfm) = %{tl_version}
Provides:       tex(ntxsups-Regular.tfm) = %{tl_version}
Provides:       tex(ntxsy.tfm) = %{tl_version}, tex(ntxsy5.tfm) = %{tl_version}
Provides:       tex(ntxsy7.tfm) = %{tl_version}, tex(ntxsybalt.tfm) = %{tl_version}
Provides:       tex(ntxsyc.tfm) = %{tl_version}, tex(ntxsym.tfm) = %{tl_version}
Provides:       tex(ntxsyralt.tfm) = %{tl_version}, tex(nxlbmi.tfm) = %{tl_version}
Provides:       tex(nxlbmi0.tfm) = %{tl_version}, tex(nxlbmi01.tfm) = %{tl_version}
Provides:       tex(nxlbmi015.tfm) = %{tl_version}, tex(nxlbmi017.tfm) = %{tl_version}
Provides:       tex(nxlbmi02.tfm) = %{tl_version}, tex(nxlbmi025.tfm) = %{tl_version}
Provides:       tex(nxlbmi027.tfm) = %{tl_version}, tex(nxlbmi03.tfm) = %{tl_version}
Provides:       tex(nxlbmi035.tfm) = %{tl_version}, tex(nxlbmi037.tfm) = %{tl_version}
Provides:       tex(nxlbmi05.tfm) = %{tl_version}, tex(nxlbmi07.tfm) = %{tl_version}
Provides:       tex(nxlbmi1.tfm) = %{tl_version}, tex(nxlbmi15.tfm) = %{tl_version}
Provides:       tex(nxlbmi17.tfm) = %{tl_version}, tex(nxlbmi2.tfm) = %{tl_version}
Provides:       tex(nxlbmi25.tfm) = %{tl_version}, tex(nxlbmi27.tfm) = %{tl_version}
Provides:       tex(nxlbmi3.tfm) = %{tl_version}, tex(nxlbmi35.tfm) = %{tl_version}
Provides:       tex(nxlbmi37.tfm) = %{tl_version}, tex(nxlbmi5.tfm) = %{tl_version}
Provides:       tex(nxlbmi7.tfm) = %{tl_version}, tex(nxlbmia.tfm) = %{tl_version}
Provides:       tex(nxlbsy5.tfm) = %{tl_version}, tex(nxlbsy7.tfm) = %{tl_version}
Provides:       tex(nxlmi.tfm) = %{tl_version}, tex(nxlmi0.tfm) = %{tl_version}
Provides:       tex(nxlmi01.tfm) = %{tl_version}, tex(nxlmi015.tfm) = %{tl_version}
Provides:       tex(nxlmi017.tfm) = %{tl_version}, tex(nxlmi02.tfm) = %{tl_version}
Provides:       tex(nxlmi025.tfm) = %{tl_version}, tex(nxlmi027.tfm) = %{tl_version}
Provides:       tex(nxlmi03.tfm) = %{tl_version}, tex(nxlmi035.tfm) = %{tl_version}
Provides:       tex(nxlmi037.tfm) = %{tl_version}, tex(nxlmi05.tfm) = %{tl_version}
Provides:       tex(nxlmi07.tfm) = %{tl_version}, tex(nxlmi1.tfm) = %{tl_version}
Provides:       tex(nxlmi15.tfm) = %{tl_version}, tex(nxlmi17.tfm) = %{tl_version}
Provides:       tex(nxlmi2.tfm) = %{tl_version}, tex(nxlmi25.tfm) = %{tl_version}
Provides:       tex(nxlmi27.tfm) = %{tl_version}, tex(nxlmi3.tfm) = %{tl_version}
Provides:       tex(nxlmi35.tfm) = %{tl_version}, tex(nxlmi37.tfm) = %{tl_version}
Provides:       tex(nxlmi5.tfm) = %{tl_version}, tex(nxlmi7.tfm) = %{tl_version}
Provides:       tex(nxlmia.tfm) = %{tl_version}, tex(nxlsy5.tfm) = %{tl_version}
Provides:       tex(nxlsy7.tfm) = %{tl_version}, tex(qtmr.tfm) = %{tl_version}
Provides:       tex(rfxlr-alt.tfm) = %{tl_version}, tex(rfxlri-alt.tfm) = %{tl_version}
Provides:       tex(rfxlri-vw.tfm) = %{tl_version}, tex(rfxlri-vw5.tfm) = %{tl_version}
Provides:       tex(rfxlri-vw7.tfm) = %{tl_version}, tex(rfxlz-alt.tfm) = %{tl_version}
Provides:       tex(rfxlzi-alt.tfm) = %{tl_version}, tex(rfxlzi-vw.tfm) = %{tl_version}
Provides:       tex(rfxlzi-vw5.tfm) = %{tl_version}, tex(rfxlzi-vw7.tfm) = %{tl_version}
Provides:       tex(rntxbmi.tfm) = %{tl_version}, tex(rntxbmi5.tfm) = %{tl_version}
Provides:       tex(rntxbmi7.tfm) = %{tl_version}, tex(rntxmi.tfm) = %{tl_version}
Provides:       tex(rntxmi5.tfm) = %{tl_version}, tex(rntxmi7.tfm) = %{tl_version}
Provides:       tex(rtxbmi-rev.tfm) = %{tl_version}, tex(rtxbmi-ut.tfm) = %{tl_version}
Provides:       tex(rtxbmi5-rev.tfm) = %{tl_version}, tex(rtxbmi5.tfm) = %{tl_version}
Provides:       tex(rtxbmi7-rev.tfm) = %{tl_version}, tex(rtxbmi7.tfm) = %{tl_version}
Provides:       tex(rtxbmio.tfm) = %{tl_version}, tex(rtxmi-ut.tfm) = %{tl_version}
Provides:       tex(rtxmi5.tfm) = %{tl_version}, tex(rtxmi7.tfm) = %{tl_version}
Provides:       tex(rtxmio.tfm) = %{tl_version}, tex(txbex-bar.tfm) = %{tl_version}
Provides:       tex(txbsy5.tfm) = %{tl_version}, tex(txbsy7.tfm) = %{tl_version}
Provides:       tex(txex-bar.tfm) = %{tl_version}, tex(txsy5.tfm) = %{tl_version}
Provides:       tex(txsy7.tfm) = %{tl_version}, tex(zmn-vw-b.tfm) = %{tl_version}
Provides:       tex(zmn-vw-r.tfm) = %{tl_version}, tex(zutbmi.tfm) = %{tl_version}
Provides:       tex(zutmi.tfm) = %{tl_version}, tex(zxlr-5nums.tfm) = %{tl_version}
Provides:       tex(zxlr-7nums.tfm) = %{tl_version}, tex(zxlr-8r.tfm) = %{tl_version}
Provides:       tex(zxlr-caps.tfm) = %{tl_version}, tex(zxlri-8r.tfm) = %{tl_version}
Provides:       tex(zxlz-8r.tfm) = %{tl_version}, tex(zxlz-caps.tfm) = %{tl_version}
Provides:       tex(zxlzi-8r.tfm) = %{tl_version}, tex(Libertine-nu.pfb) = %{tl_version}
Provides:       tex(LibertineI-5nu.pfb) = %{tl_version}, tex(LibertineI-7nu.pfb) = %{tl_version}
Provides:       tex(LibertineI-nu.pfb) = %{tl_version}, tex(LibertineTheta-Regular.pfb) = %{tl_version}
Provides:       tex(LibertineZ-nu.pfb) = %{tl_version}, tex(LibertineZI-5nu.pfb) = %{tl_version}
Provides:       tex(LibertineZI-7nu.pfb) = %{tl_version}
Provides:       tex(LibertineZI-nu.pfb) = %{tl_version}, tex(MinLibBol.pfb) = %{tl_version}
Provides:       tex(MinLibBolIta.pfb) = %{tl_version}, tex(MinLibIta.pfb) = %{tl_version}
Provides:       tex(MinLibReg.pfb) = %{tl_version}, tex(fxlri-5letters.pfb) = %{tl_version}
Provides:       tex(fxlri-7letters.pfb) = %{tl_version}, tex(fxlri-vw.pfb) = %{tl_version}
Provides:       tex(fxlri-vw5.pfb) = %{tl_version}, tex(fxlri-vw7.pfb) = %{tl_version}
Provides:       tex(fxlzi-5letters.pfb) = %{tl_version}, tex(fxlzi-7letters.pfb) = %{tl_version}
Provides:       tex(fxlzi-jv.pfb) = %{tl_version}, tex(fxlzi-jv5.pfb) = %{tl_version}
Provides:       tex(fxlzi-jv7.pfb) = %{tl_version}, tex(fxlzi-vw.pfb) = %{tl_version}
Provides:       tex(fxlzi-vw5.pfb) = %{tl_version}, tex(fxlzi-vw7.pfb) = %{tl_version}
Provides:       tex(ntxbexb.pfb) = %{tl_version}, tex(ntxbexmods.pfb) = %{tl_version}
Provides:       tex(ntxexb.pfb) = %{tl_version}, tex(ntxexmods.pfb) = %{tl_version}
Provides:       tex(ntxsups-Bold.pfb) = %{tl_version}, tex(ntxsups-BoldItalic.pfb) = %{tl_version}
Provides:       tex(ntxsups-Italic.pfb) = %{tl_version}, tex(ntxsups-Regular.pfb) = %{tl_version}
Provides:       tex(ntxsybalt.pfb) = %{tl_version}, tex(ntxsyralt.pfb) = %{tl_version}
Provides:       tex(ntxtmb.pfb) = %{tl_version}, tex(ntxtmbi.pfb) = %{tl_version}
Provides:       tex(ntxtmr.pfb) = %{tl_version}, tex(ntxtmri.pfb) = %{tl_version}
Provides:       tex(rntxbmi.pfb) = %{tl_version}, tex(rntxbmi5.pfb) = %{tl_version}
Provides:       tex(rntxbmi7.pfb) = %{tl_version}, tex(rntxmi.pfb) = %{tl_version}
Provides:       tex(rntxmi5.pfb) = %{tl_version}, tex(rntxmi7.pfb) = %{tl_version}
Provides:       tex(rtxbmi-rev.pfb) = %{tl_version}, tex(rtxbmi5-rev.pfb) = %{tl_version}
Provides:       tex(rtxbmi5.pfb) = %{tl_version}, tex(rtxbmi7-rev.pfb) = %{tl_version}
Provides:       tex(rtxbmi7.pfb) = %{tl_version}, tex(rtxmi5.pfb) = %{tl_version}
Provides:       tex(rtxmi7.pfb) = %{tl_version}, tex(txbex-bar.pfb) = %{tl_version}
Provides:       tex(txbsy5.pfb) = %{tl_version}, tex(txbsy7.pfb) = %{tl_version}
Provides:       tex(txex-bar.pfb) = %{tl_version}, tex(txsy5.pfb) = %{tl_version}
Provides:       tex(txsy7.pfb) = %{tl_version}, tex(zmn-vw-b.pfb) = %{tl_version}
Provides:       tex(zmn-vw-r.pfb) = %{tl_version}, tex(zxlr-5nums.pfb) = %{tl_version}
Provides:       tex(zxlr-7nums.pfb) = %{tl_version}, tex(zxlr.pfb) = %{tl_version}
Provides:       tex(zxlri.pfb) = %{tl_version}, tex(zxlz.pfb) = %{tl_version}
Provides:       tex(zxlzi.pfb) = %{tl_version}, tex(ntxbexa.vf) = %{tl_version}
Provides:       tex(ntxbexx.vf) = %{tl_version}, tex(ntxbmi.vf) = %{tl_version}
Provides:       tex(ntxbmi1.vf) = %{tl_version}, tex(ntxbmi15.vf) = %{tl_version}
Provides:       tex(ntxbmi17.vf) = %{tl_version}, tex(ntxbmi1x.vf) = %{tl_version}
Provides:       tex(ntxbmi5.vf) = %{tl_version}, tex(ntxbmi7.vf) = %{tl_version}
Provides:       tex(ntxbmia.vf) = %{tl_version}, tex(ntxbsy.vf) = %{tl_version}
Provides:       tex(ntxbsy5.vf) = %{tl_version}, tex(ntxbsy7.vf) = %{tl_version}
Provides:       tex(ntxbsyc.vf) = %{tl_version}, tex(ntxbsym.vf) = %{tl_version}
Provides:       tex(ntxexa.vf) = %{tl_version}, tex(ntxexx.vf) = %{tl_version}
Provides:       tex(ntxmi.vf) = %{tl_version}, tex(ntxmi1.vf) = %{tl_version}
Provides:       tex(ntxmi15.vf) = %{tl_version}, tex(ntxmi17.vf) = %{tl_version}
Provides:       tex(ntxmi5.vf) = %{tl_version}, tex(ntxmi7.vf) = %{tl_version}
Provides:       tex(ntxmia.vf) = %{tl_version}, tex(ntxsy.vf) = %{tl_version}
Provides:       tex(ntxsy5.vf) = %{tl_version}, tex(ntxsy7.vf) = %{tl_version}
Provides:       tex(ntxsyc.vf) = %{tl_version}, tex(ntxsym.vf) = %{tl_version}
Provides:       tex(nxlbmi.vf) = %{tl_version}, tex(nxlbmi0.vf) = %{tl_version}
Provides:       tex(nxlbmi01.vf) = %{tl_version}, tex(nxlbmi015.vf) = %{tl_version}
Provides:       tex(nxlbmi017.vf) = %{tl_version}, tex(nxlbmi02.vf) = %{tl_version}
Provides:       tex(nxlbmi025.vf) = %{tl_version}, tex(nxlbmi027.vf) = %{tl_version}
Provides:       tex(nxlbmi03.vf) = %{tl_version}, tex(nxlbmi035.vf) = %{tl_version}
Provides:       tex(nxlbmi037.vf) = %{tl_version}, tex(nxlbmi05.vf) = %{tl_version}
Provides:       tex(nxlbmi07.vf) = %{tl_version}, tex(nxlbmi1.vf) = %{tl_version}
Provides:       tex(nxlbmi15.vf) = %{tl_version}, tex(nxlbmi17.vf) = %{tl_version}
Provides:       tex(nxlbmi2.vf) = %{tl_version}, tex(nxlbmi25.vf) = %{tl_version}
Provides:       tex(nxlbmi27.vf) = %{tl_version}, tex(nxlbmi3.vf) = %{tl_version}
Provides:       tex(nxlbmi35.vf) = %{tl_version}, tex(nxlbmi37.vf) = %{tl_version}
Provides:       tex(nxlbmi5.vf) = %{tl_version}, tex(nxlbmi7.vf) = %{tl_version}
Provides:       tex(nxlbmia.vf) = %{tl_version}, tex(nxlbsy5.vf) = %{tl_version}
Provides:       tex(nxlbsy7.vf) = %{tl_version}, tex(nxlmi.vf) = %{tl_version}
Provides:       tex(nxlmi0.vf) = %{tl_version}, tex(nxlmi01.vf) = %{tl_version}
Provides:       tex(nxlmi015.vf) = %{tl_version}, tex(nxlmi017.vf) = %{tl_version}
Provides:       tex(nxlmi02.vf) = %{tl_version}, tex(nxlmi025.vf) = %{tl_version}
Provides:       tex(nxlmi027.vf) = %{tl_version}, tex(nxlmi03.vf) = %{tl_version}
Provides:       tex(nxlmi035.vf) = %{tl_version}, tex(nxlmi037.vf) = %{tl_version}
Provides:       tex(nxlmi05.vf) = %{tl_version}, tex(nxlmi07.vf) = %{tl_version}
Provides:       tex(nxlmi1.vf) = %{tl_version}, tex(nxlmi15.vf) = %{tl_version}
Provides:       tex(nxlmi17.vf) = %{tl_version}, tex(nxlmi2.vf) = %{tl_version}
Provides:       tex(nxlmi25.vf) = %{tl_version}, tex(nxlmi27.vf) = %{tl_version}
Provides:       tex(nxlmi3.vf) = %{tl_version}, tex(nxlmi35.vf) = %{tl_version}
Provides:       tex(nxlmi37.vf) = %{tl_version}, tex(nxlmi5.vf) = %{tl_version}
Provides:       tex(nxlmi7.vf) = %{tl_version}, tex(nxlmia.vf) = %{tl_version}
Provides:       tex(nxlsy5.vf) = %{tl_version}, tex(nxlsy7.vf) = %{tl_version}
Provides:       tex(zutbmi.vf) = %{tl_version}, tex(zutmi.vf) = %{tl_version}
Provides:       tex(ly1minlibertine.fd) = %{tl_version}, tex(ly1ntxlf.fd) = %{tl_version}
Provides:       tex(ly1ntxosf.fd) = %{tl_version}, tex(ly1ntxsups.fd) = %{tl_version}
Provides:       tex(ly1ntxtlf.fd) = %{tl_version}, tex(ly1ntxtosf.fd) = %{tl_version}
Provides:       tex(ly1ntxtt.fd) = %{tl_version}, tex(newtxmath.sty) = %{tl_version}
Provides:       tex(newtxtext.sty) = %{tl_version}, tex(omlntxmi.fd) = %{tl_version}
Provides:       tex(omlnxlmi.fd) = %{tl_version}, tex(omlzbvmi.fd) = %{tl_version}
Provides:       tex(omlzmnmi.fd) = %{tl_version}, tex(omlzutmi.fd) = %{tl_version}
Provides:       tex(ot1minlibertine.fd) = %{tl_version}, tex(ot1ntxlf.fd) = %{tl_version}
Provides:       tex(ot1ntxosf.fd) = %{tl_version}, tex(ot1ntxsups.fd) = %{tl_version}
Provides:       tex(ot1ntxtlf.fd) = %{tl_version}, tex(ot1ntxtosf.fd) = %{tl_version}
Provides:       tex(ot1ntxtt.fd) = %{tl_version}, tex(t1fxl1.fd) = %{tl_version}
Provides:       tex(t1minlibertine.fd) = %{tl_version}, tex(t1ntxlf.fd) = %{tl_version}
Provides:       tex(t1ntxosf.fd) = %{tl_version}, tex(t1ntxsups.fd) = %{tl_version}
Provides:       tex(t1ntxtlf.fd) = %{tl_version}, tex(t1ntxtosf.fd) = %{tl_version}
Provides:       tex(t1ntxtt.fd) = %{tl_version}, tex(ts1ntxlf.fd) = %{tl_version}
Provides:       tex(ts1ntxosf.fd) = %{tl_version}, tex(ts1ntxtlf.fd) = %{tl_version}
Provides:       tex(ts1ntxtosf.fd) = %{tl_version}, tex(ts1ntxtt.fd) = %{tl_version}
Provides:       tex(untxexa.fd) = %{tl_version}, tex(untxmia.fd) = %{tl_version}
Provides:       tex(untxsyc.fd) = %{tl_version}, tex(untxsym.fd) = %{tl_version}
Provides:       tex(untxtt.fd) = %{tl_version}, tex(uzmnmia.fd) = %{tl_version}

%description -n texlive-newtx
The bundle splits txfonts.sty (from the TX fonts distribution)
into two independent packages, newtxtext.sty and newtxmath.sty,
each with fixes and enhancements. newtxmath's metrics have been
re-evaluated to provide a less tight appearance, and to provide
a libertine option that substitutes Libertine italic and Greek
letter for the existing math italic and Greek glyphs, making a
mathematics package that matches Libertine text quite well.
newtxmath can also use the maths italic font provided with the
garamondx package, thus offering a garamond-alike text-with-
maths combination.

%package -n texlive-newtx-doc
Summary:        Documentation for newtx
Version:        svn47889
Provides:       tex-newtx-doc
AutoReqProv:    No

%description -n texlive-newtx-doc
Documentation for newtx

%package -n texlive-newtxsf
Provides:       tex-newtxsf = %{tl_version}
License:        OFL
Summary:        Sans-math fonts for use with newtx
Version:        svn47958
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(amsmath.sty)
Requires:       tex(xkeyval.sty), tex(binhex.tex)
Provides:       tex(newtxsf.map) = %{tl_version}, tex(ntxsfbmi.tfm) = %{tl_version}
Provides:       tex(ntxsfbmia.tfm) = %{tl_version}, tex(ntxsfmi.tfm) = %{tl_version}
Provides:       tex(ntxsfmia.tfm) = %{tl_version}, tex(zsfmi-bol.tfm) = %{tl_version}
Provides:       tex(zsfmi-reg.tfm) = %{tl_version}, tex(zsfmia-bol.tfm) = %{tl_version}
Provides:       tex(zsfmia-reg.tfm) = %{tl_version}, tex(zsfmi-bol.pfb) = %{tl_version}
Provides:       tex(zsfmi-reg.pfb) = %{tl_version}, tex(zsfmia-bol.pfb) = %{tl_version}
Provides:       tex(zsfmia-reg.pfb) = %{tl_version}, tex(ntxsfbmi.vf) = %{tl_version}
Provides:       tex(ntxsfbmia.vf) = %{tl_version}, tex(ntxsfmi.vf) = %{tl_version}
Provides:       tex(ntxsfmia.vf) = %{tl_version}, tex(newtxsf.sty) = %{tl_version}
Provides:       tex(omlntxsfmi.fd) = %{tl_version}, tex(untxsfmia.fd) = %{tl_version}

%description -n texlive-newtxsf
The package provides a maths support that amounts to
modifications of the STIX sans serif Roman and Greek letters
with most symbols taken from newtxmath (which must of course be
installed and its map file enabled).

%package -n texlive-newtxsf-doc
Summary:        Documentation for newtxsf
Version:        svn47958
Provides:       tex-newtxsf-doc
AutoReqProv:    No

%description -n texlive-newtxsf-doc
Documentation for newtxsf

%package -n texlive-newtxtt
Provides:       tex-newtxtt = %{tl_version}
License:        GPLv3+
Summary:        Enhancement of typewriter fonts from newtx
Version:        svn44510
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(fontenc.sty)
Requires:       tex(textcomp.sty), tex(xkeyval.sty)
Provides:       tex(txttAec.enc) = %{tl_version}, tex(txttAqec.enc) = %{tl_version}
Provides:       tex(txttBec.enc) = %{tl_version}, tex(txttBqec.enc) = %{tl_version}
Provides:       tex(txttCec.enc) = %{tl_version}, tex(txttCqec.enc) = %{tl_version}
Provides:       tex(txttDec.enc) = %{tl_version}, tex(txttDqec.enc) = %{tl_version}
Provides:       tex(txttEec.enc) = %{tl_version}, tex(txttEqec.enc) = %{tl_version}
Provides:       tex(newtxtt.map) = %{tl_version}, tex(newtxbtta.tfm) = %{tl_version}
Provides:       tex(newtxbttaq.tfm) = %{tl_version}, tex(newtxbttb.tfm) = %{tl_version}
Provides:       tex(newtxbttbq.tfm) = %{tl_version}, tex(newtxbttc.tfm) = %{tl_version}
Provides:       tex(newtxbttcq.tfm) = %{tl_version}, tex(newtxbttd.tfm) = %{tl_version}
Provides:       tex(newtxbttdq.tfm) = %{tl_version}, tex(newtxbtte.tfm) = %{tl_version}
Provides:       tex(newtxbtteq.tfm) = %{tl_version}, tex(newtxbttsca.tfm) = %{tl_version}
Provides:       tex(newtxbttscaq.tfm) = %{tl_version}, tex(newtxbttscb.tfm) = %{tl_version}
Provides:       tex(newtxbttscbq.tfm) = %{tl_version}, tex(newtxbttscc.tfm) = %{tl_version}
Provides:       tex(newtxbttsccq.tfm) = %{tl_version}, tex(newtxbttscd.tfm) = %{tl_version}
Provides:       tex(newtxbttscdq.tfm) = %{tl_version}, tex(newtxbttsce.tfm) = %{tl_version}
Provides:       tex(newtxbttsceq.tfm) = %{tl_version}, tex(newtxbttsla.tfm) = %{tl_version}
Provides:       tex(newtxbttslaq.tfm) = %{tl_version}, tex(newtxbttslb.tfm) = %{tl_version}
Provides:       tex(newtxbttslbq.tfm) = %{tl_version}, tex(newtxbttslc.tfm) = %{tl_version}
Provides:       tex(newtxbttslcq.tfm) = %{tl_version}, tex(newtxbttsld.tfm) = %{tl_version}
Provides:       tex(newtxbttsldq.tfm) = %{tl_version}, tex(newtxbttsle.tfm) = %{tl_version}
Provides:       tex(newtxbttsleq.tfm) = %{tl_version}, tex(newtxbttza.tfm) = %{tl_version}
Provides:       tex(newtxbttzaq.tfm) = %{tl_version}, tex(newtxbttzb.tfm) = %{tl_version}
Provides:       tex(newtxbttzbq.tfm) = %{tl_version}, tex(newtxbttzc.tfm) = %{tl_version}
Provides:       tex(newtxbttzcq.tfm) = %{tl_version}, tex(newtxbttzd.tfm) = %{tl_version}
Provides:       tex(newtxbttzdq.tfm) = %{tl_version}, tex(newtxbttze.tfm) = %{tl_version}
Provides:       tex(newtxbttzeq.tfm) = %{tl_version}, tex(newtxbttzsca.tfm) = %{tl_version}
Provides:       tex(newtxbttzscaq.tfm) = %{tl_version}, tex(newtxbttzscb.tfm) = %{tl_version}
Provides:       tex(newtxbttzscbq.tfm) = %{tl_version}, tex(newtxbttzscc.tfm) = %{tl_version}
Provides:       tex(newtxbttzsccq.tfm) = %{tl_version}, tex(newtxbttzscd.tfm) = %{tl_version}
Provides:       tex(newtxbttzscdq.tfm) = %{tl_version}, tex(newtxbttzsce.tfm) = %{tl_version}
Provides:       tex(newtxbttzsceq.tfm) = %{tl_version}, tex(newtxbttzsla.tfm) = %{tl_version}
Provides:       tex(newtxbttzslaq.tfm) = %{tl_version}, tex(newtxbttzslb.tfm) = %{tl_version}
Provides:       tex(newtxbttzslbq.tfm) = %{tl_version}, tex(newtxbttzslc.tfm) = %{tl_version}
Provides:       tex(newtxbttzslcq.tfm) = %{tl_version}, tex(newtxbttzsld.tfm) = %{tl_version}
Provides:       tex(newtxbttzsldq.tfm) = %{tl_version}, tex(newtxbttzsle.tfm) = %{tl_version}
Provides:       tex(newtxbttzsleq.tfm) = %{tl_version}, tex(newtxtta.tfm) = %{tl_version}
Provides:       tex(newtxttaq.tfm) = %{tl_version}, tex(newtxttb.tfm) = %{tl_version}
Provides:       tex(newtxttbq.tfm) = %{tl_version}, tex(newtxttc.tfm) = %{tl_version}
Provides:       tex(newtxttcq.tfm) = %{tl_version}, tex(newtxttd.tfm) = %{tl_version}
Provides:       tex(newtxttdq.tfm) = %{tl_version}, tex(newtxtte.tfm) = %{tl_version}
Provides:       tex(newtxtteq.tfm) = %{tl_version}, tex(newtxttsca.tfm) = %{tl_version}
Provides:       tex(newtxttscaq.tfm) = %{tl_version}, tex(newtxttscb.tfm) = %{tl_version}
Provides:       tex(newtxttscbq.tfm) = %{tl_version}, tex(newtxttscc.tfm) = %{tl_version}
Provides:       tex(newtxttsccq.tfm) = %{tl_version}, tex(newtxttscd.tfm) = %{tl_version}
Provides:       tex(newtxttscdq.tfm) = %{tl_version}, tex(newtxttsce.tfm) = %{tl_version}
Provides:       tex(newtxttsceq.tfm) = %{tl_version}, tex(newtxttsla.tfm) = %{tl_version}
Provides:       tex(newtxttslaq.tfm) = %{tl_version}, tex(newtxttslb.tfm) = %{tl_version}
Provides:       tex(newtxttslbq.tfm) = %{tl_version}, tex(newtxttslc.tfm) = %{tl_version}
Provides:       tex(newtxttslcq.tfm) = %{tl_version}, tex(newtxttsld.tfm) = %{tl_version}
Provides:       tex(newtxttsldq.tfm) = %{tl_version}, tex(newtxttsle.tfm) = %{tl_version}
Provides:       tex(newtxttsleq.tfm) = %{tl_version}, tex(newtxttza.tfm) = %{tl_version}
Provides:       tex(newtxttzaq.tfm) = %{tl_version}, tex(newtxttzb.tfm) = %{tl_version}
Provides:       tex(newtxttzbq.tfm) = %{tl_version}, tex(newtxttzc.tfm) = %{tl_version}
Provides:       tex(newtxttzcq.tfm) = %{tl_version}, tex(newtxttzd.tfm) = %{tl_version}
Provides:       tex(newtxttzdq.tfm) = %{tl_version}, tex(newtxttze.tfm) = %{tl_version}
Provides:       tex(newtxttzeq.tfm) = %{tl_version}, tex(newtxttzsca.tfm) = %{tl_version}
Provides:       tex(newtxttzscaq.tfm) = %{tl_version}, tex(newtxttzscb.tfm) = %{tl_version}
Provides:       tex(newtxttzscbq.tfm) = %{tl_version}, tex(newtxttzscc.tfm) = %{tl_version}
Provides:       tex(newtxttzsccq.tfm) = %{tl_version}, tex(newtxttzscd.tfm) = %{tl_version}
Provides:       tex(newtxttzscdq.tfm) = %{tl_version}, tex(newtxttzsce.tfm) = %{tl_version}
Provides:       tex(newtxttzsceq.tfm) = %{tl_version}, tex(newtxttzsla.tfm) = %{tl_version}
Provides:       tex(newtxttzslaq.tfm) = %{tl_version}, tex(newtxttzslb.tfm) = %{tl_version}
Provides:       tex(newtxttzslbq.tfm) = %{tl_version}, tex(newtxttzslc.tfm) = %{tl_version}
Provides:       tex(newtxttzslcq.tfm) = %{tl_version}, tex(newtxttzsld.tfm) = %{tl_version}
Provides:       tex(newtxttzsldq.tfm) = %{tl_version}, tex(newtxttzsle.tfm) = %{tl_version}
Provides:       tex(newtxttzsleq.tfm) = %{tl_version}, tex(tcxbttz.tfm) = %{tl_version}
Provides:       tex(tcxbttzsl.tfm) = %{tl_version}, tex(tcxttz.tfm) = %{tl_version}
Provides:       tex(tcxttzsl.tfm) = %{tl_version}, tex(newtxbtt.pfb) = %{tl_version}
Provides:       tex(newtxbttsc.pfb) = %{tl_version}, tex(newtxtt.pfb) = %{tl_version}
Provides:       tex(newtxttsc.pfb) = %{tl_version}, tex(newtxtt.sty) = %{tl_version}
Provides:       tex(t1newtxtt.fd) = %{tl_version}, tex(t1newtxttz.fd) = %{tl_version}
Provides:       tex(ts1newtxtt.fd) = %{tl_version}, tex(ts1newtxttz.fd) = %{tl_version}

%description -n texlive-newtxtt
The package provides enhanced fonts with LaTeX support files
providing access to the typewriter fonts from newtx. Regular
and bold weights, slanted variants and a choice of four
different styles for zero.

%package -n texlive-newtxtt-doc
Summary:        Documentation for newtxtt
Version:        svn44510
Provides:       tex-newtxtt-doc
AutoReqProv:    No

%description -n texlive-newtxtt-doc
Documentation for newtxtt

%package -n texlive-nkarta
Provides:       tex-nkarta = %{tl_version}
License:        Public Domain
Summary:        A "new" version of the karta cartographic fonts
Version:        svn16437.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(nkarta15.tfm) = %{tl_version}

%description -n texlive-nkarta
A development of the karta font, offering more mathematical
stability in Metafont. A version that will produce the glyphs
as Encapsulated PostScript, using MetaPost, is also provided.

%package -n texlive-nkarta-doc
Summary:        Documentation for nkarta
Version:        svn16437.0.2

Provides:       tex-nkarta-doc
AutoReqProv:    No

%description -n texlive-nkarta-doc
Documentation for nkarta

%package -n texlive-ncntrsbk
Provides:       tex-ncntrsbk = %{tl_version}
License:        GPL+
Summary:        URW "Base 35" font pack for LaTeX
Version:        svn31835.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(unc.map) = %{tl_version}, tex(pncb.tfm) = %{tl_version}
Provides:       tex(pncb7t.tfm) = %{tl_version}, tex(pncb8c.tfm) = %{tl_version}
Provides:       tex(pncb8r.tfm) = %{tl_version}, tex(pncb8t.tfm) = %{tl_version}
Provides:       tex(pncbc.tfm) = %{tl_version}, tex(pncbc7t.tfm) = %{tl_version}
Provides:       tex(pncbc8t.tfm) = %{tl_version}, tex(pncbi.tfm) = %{tl_version}
Provides:       tex(pncbi7t.tfm) = %{tl_version}, tex(pncbi8c.tfm) = %{tl_version}
Provides:       tex(pncbi8r.tfm) = %{tl_version}, tex(pncbi8t.tfm) = %{tl_version}
Provides:       tex(pncbo.tfm) = %{tl_version}, tex(pncbo7t.tfm) = %{tl_version}
Provides:       tex(pncbo8c.tfm) = %{tl_version}, tex(pncbo8r.tfm) = %{tl_version}
Provides:       tex(pncbo8t.tfm) = %{tl_version}, tex(pncr.tfm) = %{tl_version}
Provides:       tex(pncr7t.tfm) = %{tl_version}, tex(pncr8c.tfm) = %{tl_version}
Provides:       tex(pncr8r.tfm) = %{tl_version}, tex(pncr8t.tfm) = %{tl_version}
Provides:       tex(pncrc.tfm) = %{tl_version}, tex(pncrc7t.tfm) = %{tl_version}
Provides:       tex(pncrc8t.tfm) = %{tl_version}, tex(pncri.tfm) = %{tl_version}
Provides:       tex(pncri7t.tfm) = %{tl_version}, tex(pncri8c.tfm) = %{tl_version}
Provides:       tex(pncri8r.tfm) = %{tl_version}, tex(pncri8t.tfm) = %{tl_version}
Provides:       tex(pncro.tfm) = %{tl_version}, tex(pncro7t.tfm) = %{tl_version}
Provides:       tex(pncro8c.tfm) = %{tl_version}, tex(pncro8r.tfm) = %{tl_version}
Provides:       tex(pncro8t.tfm) = %{tl_version}, tex(uncb7t.tfm) = %{tl_version}
Provides:       tex(uncb8c.tfm) = %{tl_version}, tex(uncb8r.tfm) = %{tl_version}
Provides:       tex(uncb8t.tfm) = %{tl_version}, tex(uncbc7t.tfm) = %{tl_version}
Provides:       tex(uncbc8t.tfm) = %{tl_version}, tex(uncbi7t.tfm) = %{tl_version}
Provides:       tex(uncbi8c.tfm) = %{tl_version}, tex(uncbi8r.tfm) = %{tl_version}
Provides:       tex(uncbi8t.tfm) = %{tl_version}, tex(uncbo7t.tfm) = %{tl_version}
Provides:       tex(uncbo8c.tfm) = %{tl_version}, tex(uncbo8r.tfm) = %{tl_version}
Provides:       tex(uncbo8t.tfm) = %{tl_version}, tex(uncr7t.tfm) = %{tl_version}
Provides:       tex(uncr8c.tfm) = %{tl_version}, tex(uncr8r.tfm) = %{tl_version}
Provides:       tex(uncr8t.tfm) = %{tl_version}, tex(uncrc7t.tfm) = %{tl_version}
Provides:       tex(uncrc8t.tfm) = %{tl_version}, tex(uncri7t.tfm) = %{tl_version}
Provides:       tex(uncri8c.tfm) = %{tl_version}, tex(uncri8r.tfm) = %{tl_version}
Provides:       tex(uncri8t.tfm) = %{tl_version}, tex(uncro7t.tfm) = %{tl_version}
Provides:       tex(uncro8c.tfm) = %{tl_version}, tex(uncro8r.tfm) = %{tl_version}
Provides:       tex(uncro8t.tfm) = %{tl_version}, tex(uncb8a.pfb) = %{tl_version}
Provides:       tex(uncbi8a.pfb) = %{tl_version}, tex(uncr8a.pfb) = %{tl_version}
Provides:       tex(uncri8a.pfb) = %{tl_version}, tex(pncb.vf) = %{tl_version}
Provides:       tex(pncb7t.vf) = %{tl_version}, tex(pncb8c.vf) = %{tl_version}
Provides:       tex(pncb8t.vf) = %{tl_version}, tex(pncbc.vf) = %{tl_version}
Provides:       tex(pncbc7t.vf) = %{tl_version}, tex(pncbc8t.vf) = %{tl_version}
Provides:       tex(pncbi.vf) = %{tl_version}, tex(pncbi7t.vf) = %{tl_version}
Provides:       tex(pncbi8c.vf) = %{tl_version}, tex(pncbi8t.vf) = %{tl_version}
Provides:       tex(pncbo.vf) = %{tl_version}, tex(pncbo7t.vf) = %{tl_version}
Provides:       tex(pncbo8c.vf) = %{tl_version}, tex(pncbo8t.vf) = %{tl_version}
Provides:       tex(pncr.vf) = %{tl_version}, tex(pncr7t.vf) = %{tl_version}
Provides:       tex(pncr8c.vf) = %{tl_version}, tex(pncr8t.vf) = %{tl_version}
Provides:       tex(pncrc.vf) = %{tl_version}, tex(pncrc7t.vf) = %{tl_version}
Provides:       tex(pncrc8t.vf) = %{tl_version}, tex(pncri.vf) = %{tl_version}
Provides:       tex(pncri7t.vf) = %{tl_version}, tex(pncri8c.vf) = %{tl_version}
Provides:       tex(pncri8t.vf) = %{tl_version}, tex(pncro.vf) = %{tl_version}
Provides:       tex(pncro7t.vf) = %{tl_version}, tex(pncro8c.vf) = %{tl_version}
Provides:       tex(pncro8t.vf) = %{tl_version}, tex(uncb7t.vf) = %{tl_version}
Provides:       tex(uncb8c.vf) = %{tl_version}, tex(uncb8t.vf) = %{tl_version}
Provides:       tex(uncbc7t.vf) = %{tl_version}, tex(uncbc8t.vf) = %{tl_version}
Provides:       tex(uncbi7t.vf) = %{tl_version}, tex(uncbi8c.vf) = %{tl_version}
Provides:       tex(uncbi8t.vf) = %{tl_version}, tex(uncbo7t.vf) = %{tl_version}
Provides:       tex(uncbo8c.vf) = %{tl_version}, tex(uncbo8t.vf) = %{tl_version}
Provides:       tex(uncr7t.vf) = %{tl_version}, tex(uncr8c.vf) = %{tl_version}
Provides:       tex(uncr8t.vf) = %{tl_version}, tex(uncrc7t.vf) = %{tl_version}
Provides:       tex(uncrc8t.vf) = %{tl_version}, tex(uncri7t.vf) = %{tl_version}
Provides:       tex(uncri8c.vf) = %{tl_version}, tex(uncri8t.vf) = %{tl_version}
Provides:       tex(uncro7t.vf) = %{tl_version}, tex(uncro8c.vf) = %{tl_version}
Provides:       tex(uncro8t.vf) = %{tl_version}, tex(8runc.fd) = %{tl_version}
Provides:       tex(omlunc.fd) = %{tl_version}, tex(omsunc.fd) = %{tl_version}
Provides:       tex(ot1unc.fd) = %{tl_version}, tex(t1unc.fd) = %{tl_version}
Provides:       tex(ts1unc.fd) = %{tl_version}

%description -n texlive-ncntrsbk
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).


%package -n texlive-navigator
Provides:       tex-navigator = %{tl_version}
License:        LPPL
Summary:        PDF features across formats and engines
Version:        svn41413

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(navigator.sty) = %{tl_version}, tex(navigator.tex) = %{tl_version}
Provides:       tex(t-navigator.tex) = %{tl_version}

%description -n texlive-navigator
Navigator implements PDF features for all formats (with some
limitations in ConTeXt) with PDFTeX, LuaTeX and XeTeX (i.e.
xdvipdfmx). Features include: Customizable outlines (i.e.
bookmarks); Anchors; Links and actions (e.g. JavaScript or user-
defined PDF actions); File embedding (not in ConTeXt); Document
information and PDF viewer's display (not in ConTeXt); and
Commands to create and use raw PDF objects. Navigator requires
texapi and yax, both version at least 1.03.

%package -n texlive-navigator-doc
Summary:        Documentation for navigator
Version:        svn41413

Provides:       tex-navigator-doc
AutoReqProv:    No

%description -n texlive-navigator-doc
Documentation for navigator

%package -n texlive-multido
Provides:       tex-multido = %{tl_version}
License:        LPPL
Summary:        A loop facility for Generic TeX
Version:        svn18302.1.42

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(multido.tex) = %{tl_version}, tex(multido.sty) = %{tl_version}

%description -n texlive-multido
The package provides the \multido command, which was originally
designed for use with PSTricks. Fixed-point arithmetic is used
when working on the loop variable, so that the package is
equally applicable in graphics applications like PSTricks as it
is with the more common integer loops.

%package -n texlive-multido-doc
Summary:        Documentation for multido
Version:        svn18302.1.42

Provides:       tex-multido-doc
AutoReqProv:    No

%description -n texlive-multido-doc
Documentation for multido

%package -n texlive-ncctools
Provides:       tex-ncctools = %{tl_version}
License:        LPPL
Summary:        A collection of general packages for LaTeX
Version:        svn48127
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(perpage.sty), tex(amsmath.sty), tex(graphicx.sty), tex(amsgen.sty)
Provides:       tex(afterpackage.sty) = %{tl_version}, tex(dcounter.sty) = %{tl_version}
Provides:       tex(desclist.sty) = %{tl_version}, tex(extdash.sty) = %{tl_version}
Provides:       tex(manyfoot.sty) = %{tl_version}, tex(mboxfill.sty) = %{tl_version}
Provides:       tex(nccbbb.sty) = %{tl_version}, tex(nccboxes.sty) = %{tl_version}
Provides:       tex(ncccomma.sty) = %{tl_version}, tex(ncccropbox.sty) = %{tl_version}
Provides:       tex(ncccropmark.sty) = %{tl_version}, tex(nccfancyhdr.sty) = %{tl_version}
Provides:       tex(nccfloats.sty) = %{tl_version}, tex(nccfoots.sty) = %{tl_version}
Provides:       tex(nccmath.sty) = %{tl_version}, tex(nccparskip.sty) = %{tl_version}
Provides:       tex(nccpic.sty) = %{tl_version}, tex(nccrules.sty) = %{tl_version}
Provides:       tex(nccsect.sty) = %{tl_version}, tex(nccstretch.sty) = %{tl_version}
Provides:       tex(nccthm.sty) = %{tl_version}, tex(textarea.sty) = %{tl_version}
Provides:       tex(tocenter.sty) = %{tl_version}, tex(topsection.sty) = %{tl_version}
Provides:       tex(watermark.sty) = %{tl_version}

%description -n texlive-ncctools
The NCCtools bundle contains many packages for general use
under LaTeX; many are also used by NCC LaTeX. The bundle
includes tools for: executing commands after a package is
loaded; watermarks; counter manipulation (dynamic counters,
changing counter numbering with another counter); improvements
to the description environment; hyphenation of compound words;
new levels of footnotes; space-filling patterns; "poor man's"
Black Board Bold symbols; alignment of the content of a box;
use comma as decimal separator; boxes with their own crop
marks; page cropmarks; improvements to fancy headers; float
"styles", mini floats, side floats; manually marked footnotes;
extension of amsmath; control of paragraph skip; an envelope to
the graphicx package; dashed and multiple rules; alternative
techniques for declarations of sections, captions, and toc-
entries; generalised text-stretching; generation of new theorem-
like environments; control of the text area; centred page
layouts; and un-numbered top-level section.

%package -n texlive-ncctools-doc
Summary:        Documentation for ncctools
Version:        svn48127
Provides:       tex-ncctools-doc
AutoReqProv:    No

%description -n texlive-ncctools-doc
Documentation for ncctools

%package -n texlive-mongolian-babel
Provides:       tex-mongolian-babel = %{tl_version}
License:        LPPL
Summary:        A language definition file for Mongolian in Babel
Version:        svn15878.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mn.def) = %{tl_version}, tex(mongolian.ldf) = %{tl_version}
Provides:       tex(mongolian.sty) = %{tl_version}

%description -n texlive-mongolian-babel
This package provides support for Mongolian in a Cyrillic
alphabet. (The work derives from the earlier Russian work for
babel.)

%package -n texlive-mongolian-babel-doc
Summary:        Documentation for mongolian-babel
Version:        svn15878.1.2

Provides:       tex-mongolian-babel-doc
AutoReqProv:    No

%description -n texlive-mongolian-babel-doc
Documentation for mongolian-babel

%package -n texlive-montex
Provides:       tex-montex = %{tl_version}
License:        GPL+
Summary:        Mongolian LaTeX
Version:        svn29349.IVu.04.092

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex-cbfonts, tex(ifthen.sty), tex(diagnose.sty), tex(fontenc.sty)
Requires:       tex(inputenc.sty), tex(rotating.sty), tex(lscape.sty)
Provides:       tex(mongolian.map) = %{tl_version}, tex(bcghsb.tfm) = %{tl_version}
Provides:       tex(bcghsm.tfm) = %{tl_version}, tex(bcghwb.tfm) = %{tl_version}
Provides:       tex(bcghwm.tfm) = %{tl_version}, tex(bcgvsb.tfm) = %{tl_version}
Provides:       tex(bcgvsm.tfm) = %{tl_version}, tex(bcgvwb.tfm) = %{tl_version}
Provides:       tex(bcgvwm.tfm) = %{tl_version}, tex(bicighb.tfm) = %{tl_version}
Provides:       tex(bicighm.tfm) = %{tl_version}, tex(bicigvb.tfm) = %{tl_version}
Provides:       tex(bicigvm.tfm) = %{tl_version}, tex(bthhsb.tfm) = %{tl_version}
Provides:       tex(bthhsm.tfm) = %{tl_version}, tex(bthhwb.tfm) = %{tl_version}
Provides:       tex(bthhwm.tfm) = %{tl_version}, tex(bthvsb.tfm) = %{tl_version}
Provides:       tex(bthvsm.tfm) = %{tl_version}, tex(bthvwb.tfm) = %{tl_version}
Provides:       tex(bthvwm.tfm) = %{tl_version}, tex(bxghsb.tfm) = %{tl_version}
Provides:       tex(bxghsm.tfm) = %{tl_version}, tex(bxghwb.tfm) = %{tl_version}
Provides:       tex(bxghwm.tfm) = %{tl_version}, tex(bxgvsb.tfm) = %{tl_version}
Provides:       tex(bxgvsm.tfm) = %{tl_version}, tex(bxgvwb.tfm) = %{tl_version}
Provides:       tex(bxgvwm.tfm) = %{tl_version}, tex(kmb10.tfm) = %{tl_version}
Provides:       tex(kmbx10.tfm) = %{tl_version}, tex(kmbx12.tfm) = %{tl_version}
Provides:       tex(kmbx5.tfm) = %{tl_version}, tex(kmbx6.tfm) = %{tl_version}
Provides:       tex(kmbx7.tfm) = %{tl_version}, tex(kmbx8.tfm) = %{tl_version}
Provides:       tex(kmbx9.tfm) = %{tl_version}, tex(kmbxsl10.tfm) = %{tl_version}
Provides:       tex(kmbxti10.tfm) = %{tl_version}, tex(kmcsc10.tfm) = %{tl_version}
Provides:       tex(kmcsc8.tfm) = %{tl_version}, tex(kmcsc9.tfm) = %{tl_version}
Provides:       tex(kmdunh10.tfm) = %{tl_version}, tex(kmff10.tfm) = %{tl_version}
Provides:       tex(kmfi10.tfm) = %{tl_version}, tex(kmfib8.tfm) = %{tl_version}
Provides:       tex(kminch.tfm) = %{tl_version}, tex(kmitt10.tfm) = %{tl_version}
Provides:       tex(kmr10.tfm) = %{tl_version}, tex(kmr12.tfm) = %{tl_version}
Provides:       tex(kmr17.tfm) = %{tl_version}, tex(kmr5.tfm) = %{tl_version}
Provides:       tex(kmr6.tfm) = %{tl_version}, tex(kmr7.tfm) = %{tl_version}
Provides:       tex(kmr8.tfm) = %{tl_version}, tex(kmr9.tfm) = %{tl_version}
Provides:       tex(kmsl10.tfm) = %{tl_version}, tex(kmsl12.tfm) = %{tl_version}
Provides:       tex(kmsl8.tfm) = %{tl_version}, tex(kmsl9.tfm) = %{tl_version}
Provides:       tex(kmsltt10.tfm) = %{tl_version}, tex(kmss10.tfm) = %{tl_version}
Provides:       tex(kmss12.tfm) = %{tl_version}, tex(kmss17.tfm) = %{tl_version}
Provides:       tex(kmss8.tfm) = %{tl_version}, tex(kmss9.tfm) = %{tl_version}
Provides:       tex(kmssbx10.tfm) = %{tl_version}, tex(kmssdc10.tfm) = %{tl_version}
Provides:       tex(kmssi10.tfm) = %{tl_version}, tex(kmssi12.tfm) = %{tl_version}
Provides:       tex(kmssi17.tfm) = %{tl_version}, tex(kmssi8.tfm) = %{tl_version}
Provides:       tex(kmssi9.tfm) = %{tl_version}, tex(kmssq8.tfm) = %{tl_version}
Provides:       tex(kmssqi8.tfm) = %{tl_version}, tex(kmtcsc10.tfm) = %{tl_version}
Provides:       tex(kmti10.tfm) = %{tl_version}, tex(kmti12.tfm) = %{tl_version}
Provides:       tex(kmti7.tfm) = %{tl_version}, tex(kmti8.tfm) = %{tl_version}
Provides:       tex(kmti9.tfm) = %{tl_version}, tex(kmtt10.tfm) = %{tl_version}
Provides:       tex(kmtt12.tfm) = %{tl_version}, tex(kmtt8.tfm) = %{tl_version}
Provides:       tex(kmtt9.tfm) = %{tl_version}, tex(kmu10.tfm) = %{tl_version}
Provides:       tex(kmvtt10.tfm) = %{tl_version}, tex(kmvtti10.tfm) = %{tl_version}
Provides:       tex(bcghsb.pfb) = %{tl_version}, tex(bcghsm.pfb) = %{tl_version}
Provides:       tex(bcghwb.pfb) = %{tl_version}, tex(bcghwm.pfb) = %{tl_version}
Provides:       tex(bcgvsb.pfb) = %{tl_version}, tex(bcgvsm.pfb) = %{tl_version}
Provides:       tex(bcgvwb.pfb) = %{tl_version}, tex(bcgvwm.pfb) = %{tl_version}
Provides:       tex(bicighb.pfb) = %{tl_version}, tex(bicighm.pfb) = %{tl_version}
Provides:       tex(bicigvb.pfb) = %{tl_version}, tex(bicigvm.pfb) = %{tl_version}
Provides:       tex(bthhsb.pfb) = %{tl_version}, tex(bthhsm.pfb) = %{tl_version}
Provides:       tex(bthhwb.pfb) = %{tl_version}, tex(bthhwm.pfb) = %{tl_version}
Provides:       tex(bthvsb.pfb) = %{tl_version}, tex(bthvsm.pfb) = %{tl_version}
Provides:       tex(bthvwb.pfb) = %{tl_version}, tex(bthvwm.pfb) = %{tl_version}
Provides:       tex(bxghsb.pfb) = %{tl_version}, tex(bxghsm.pfb) = %{tl_version}
Provides:       tex(bxghwb.pfb) = %{tl_version}, tex(bxghwm.pfb) = %{tl_version}
Provides:       tex(bxgvsb.pfb) = %{tl_version}, tex(bxgvsm.pfb) = %{tl_version}
Provides:       tex(bxgvwb.pfb) = %{tl_version}, tex(bxgvwm.pfb) = %{tl_version}
Provides:       tex(kmbx10.pfb) = %{tl_version}, tex(kmr10.pfb) = %{tl_version}
Provides:       tex(kmss10.pfb) = %{tl_version}, tex(bicig.def) = %{tl_version}
Provides:       tex(bithe.def) = %{tl_version}, tex(buryat.def) = %{tl_version}
Provides:       tex(cpctt.def) = %{tl_version}, tex(cpdbk.def) = %{tl_version}
Provides:       tex(cpibmrus.def) = %{tl_version}, tex(cpkoi.def) = %{tl_version}
Provides:       tex(cpmls.def) = %{tl_version}, tex(cpmnk.def) = %{tl_version}
Provides:       tex(cpmos.def) = %{tl_version}, tex(cpncc.def) = %{tl_version}
Provides:       tex(english.def) = %{tl_version}, tex(kazakh.def) = %{tl_version}
Provides:       tex(lmabthhs.fd) = %{tl_version}, tex(lmabthhw.fd) = %{tl_version}
Provides:       tex(lmabthvs.fd) = %{tl_version}, tex(lmabthvw.fd) = %{tl_version}
Provides:       tex(lmaenc.def) = %{tl_version}, tex(lmccmdh.fd) = %{tl_version}
Provides:       tex(lmccmfib.fd) = %{tl_version}, tex(lmccmfr.fd) = %{tl_version}
Provides:       tex(lmccmiss.fd) = %{tl_version}, tex(lmccmr.fd) = %{tl_version}
Provides:       tex(lmccmss.fd) = %{tl_version}, tex(lmccmssq.fd) = %{tl_version}
Provides:       tex(lmccmtt.fd) = %{tl_version}, tex(lmccmvtt.fd) = %{tl_version}
Provides:       tex(lmcenc.def) = %{tl_version}, tex(lmclcmss.fd) = %{tl_version}
Provides:       tex(lmobcghs.fd) = %{tl_version}, tex(lmobcghw.fd) = %{tl_version}
Provides:       tex(lmobcgvs.fd) = %{tl_version}, tex(lmobcgvw.fd) = %{tl_version}
Provides:       tex(lmoenc.def) = %{tl_version}, tex(lmsbcgh.fd) = %{tl_version}
Provides:       tex(lmsbcgv.fd) = %{tl_version}, tex(lmsenc.def) = %{tl_version}
Provides:       tex(lmubxghs.fd) = %{tl_version}, tex(lmubxghw.fd) = %{tl_version}
Provides:       tex(lmubxgvs.fd) = %{tl_version}, tex(lmubxgvw.fd) = %{tl_version}
Provides:       tex(lmuenc.def) = %{tl_version}, tex(mls.sty) = %{tl_version}
Provides:       tex(mlsgalig.tex) = %{tl_version}, tex(mlstrans.tex) = %{tl_version}
Provides:       tex(mnhyphex.tex) = %{tl_version}, tex(rlbicig.sty) = %{tl_version}
Provides:       tex(russian.def) = %{tl_version}, tex(xalx.def) = %{tl_version}

%description -n texlive-montex
MonTeX provides Mongolian and Manju support for the TeX/LaTeX
community. Mongolian is a language spoken in North East Asia,
namely Mongolia and the Inner Mongol Autonomous Region of
China. Today, it is written in an extended Cyrillic alphabet in
Mongolia whereas the Uighur writing continues to be in use in
Inner Mongolia, though it is also, legally speaking, the
official writing system of Mongolia. Manju is another language
of North East Asia, belonging to the Tungusic branch of the
Altaic languages. Though it is hardly spoken nowadays, it
survives in written form as Manju was the native language of
the rulers of the Qing dynasty (1644-1911) in China. Large
quantities of documents of the Imperial Archives survive, as
well as some of the finest dictionaries ever compiled in Asia,
like the Pentaglot, a dictionary comprising Manju, Tibetan,
Mongolian, Uighur and Chinese. MonTeX provides all necessary
characters for writing standard Mongolian in Cyrillic and
Classical (aka Traditional or Uighur) writing, and Manju as
well as transliterated Tibetan texts, for which purpose a
number of additional characters was created. In MonTeX, both
Mongolian and Manju are entered in romanized form. The
retransliteration (from Latin input to Mongolian and Manju
output) is completely realized in TeX/Metafont so that no
external preprocessor is required. Please note that most of the
enhanced functions of MonTeX require a working e-LaTeX
environment. This is especially true when compiling documents
with Mongolian or Manju as the main document language. It is
recommended to choose pdfelatex as the resulting PDF files are
truly portable. Vertical text generated by MonTeX is not
supported in DVI.

%package -n texlive-montex-doc
Summary:        Documentation for montex
Version:        svn29349.IVu.04.092

Provides:       tex-montex-doc
AutoReqProv:    No
Requires:       tex-cbfonts-doc

%description -n texlive-montex-doc
Documentation for montex

%package -n texlive-mpman-ru-doc
Summary:        Documentation for mpman-ru
Version:        svn15878.1.004

Provides:       tex-mpman-ru-doc
AutoReqProv:    No

%description -n texlive-mpman-ru-doc
Documentation for mpman-ru

%package -n texlive-nevelok
Provides:       tex-nevelok = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX package for automatic definite articles for Hungarian
Version:        svn39029

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xstring.sty)
Provides:       tex(nevelok.sty) = %{tl_version}

%description -n texlive-nevelok
LaTeX package for automatic definite articles for Hungarian

%package -n texlive-nevelok-doc
Summary:        Documentation for nevelok
Version:        svn39029

Provides:       tex-nevelok-doc
AutoReqProv:    No

%description -n texlive-nevelok-doc
Documentation for nevelok

%package -n texlive-nanumtype1
Provides:       tex-nanumtype1 = %{tl_version}
License:        OFL
Summary:        Type1 subfonts of Nanum Korean fonts
Version:        svn29558.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(nanumfonts.map) = %{tl_version}, tex(nanumgtb00.tfm) = %{tl_version}
Provides:       tex(nanumgtb01.tfm) = %{tl_version}, tex(nanumgtb02.tfm) = %{tl_version}
Provides:       tex(nanumgtb03.tfm) = %{tl_version}, tex(nanumgtb04.tfm) = %{tl_version}
Provides:       tex(nanumgtb11.tfm) = %{tl_version}, tex(nanumgtb20.tfm) = %{tl_version}
Provides:       tex(nanumgtb21.tfm) = %{tl_version}, tex(nanumgtb22.tfm) = %{tl_version}
Provides:       tex(nanumgtb23.tfm) = %{tl_version}, tex(nanumgtb24.tfm) = %{tl_version}
Provides:       tex(nanumgtb25.tfm) = %{tl_version}, tex(nanumgtb26.tfm) = %{tl_version}
Provides:       tex(nanumgtb27.tfm) = %{tl_version}, tex(nanumgtb2a.tfm) = %{tl_version}
Provides:       tex(nanumgtb30.tfm) = %{tl_version}, tex(nanumgtb31.tfm) = %{tl_version}
Provides:       tex(nanumgtb32.tfm) = %{tl_version}, tex(nanumgtb33.tfm) = %{tl_version}
Provides:       tex(nanumgtb4e.tfm) = %{tl_version}, tex(nanumgtb4f.tfm) = %{tl_version}
Provides:       tex(nanumgtb50.tfm) = %{tl_version}, tex(nanumgtb51.tfm) = %{tl_version}
Provides:       tex(nanumgtb52.tfm) = %{tl_version}, tex(nanumgtb53.tfm) = %{tl_version}
Provides:       tex(nanumgtb54.tfm) = %{tl_version}, tex(nanumgtb55.tfm) = %{tl_version}
Provides:       tex(nanumgtb56.tfm) = %{tl_version}, tex(nanumgtb57.tfm) = %{tl_version}
Provides:       tex(nanumgtb58.tfm) = %{tl_version}, tex(nanumgtb59.tfm) = %{tl_version}
Provides:       tex(nanumgtb5a.tfm) = %{tl_version}, tex(nanumgtb5b.tfm) = %{tl_version}
Provides:       tex(nanumgtb5c.tfm) = %{tl_version}, tex(nanumgtb5d.tfm) = %{tl_version}
Provides:       tex(nanumgtb5e.tfm) = %{tl_version}, tex(nanumgtb5f.tfm) = %{tl_version}
Provides:       tex(nanumgtb60.tfm) = %{tl_version}, tex(nanumgtb61.tfm) = %{tl_version}
Provides:       tex(nanumgtb62.tfm) = %{tl_version}, tex(nanumgtb63.tfm) = %{tl_version}
Provides:       tex(nanumgtb64.tfm) = %{tl_version}, tex(nanumgtb65.tfm) = %{tl_version}
Provides:       tex(nanumgtb66.tfm) = %{tl_version}, tex(nanumgtb67.tfm) = %{tl_version}
Provides:       tex(nanumgtb68.tfm) = %{tl_version}, tex(nanumgtb69.tfm) = %{tl_version}
Provides:       tex(nanumgtb6a.tfm) = %{tl_version}, tex(nanumgtb6b.tfm) = %{tl_version}
Provides:       tex(nanumgtb6c.tfm) = %{tl_version}, tex(nanumgtb6d.tfm) = %{tl_version}
Provides:       tex(nanumgtb6e.tfm) = %{tl_version}, tex(nanumgtb6f.tfm) = %{tl_version}
Provides:       tex(nanumgtb70.tfm) = %{tl_version}, tex(nanumgtb71.tfm) = %{tl_version}
Provides:       tex(nanumgtb72.tfm) = %{tl_version}, tex(nanumgtb73.tfm) = %{tl_version}
Provides:       tex(nanumgtb74.tfm) = %{tl_version}, tex(nanumgtb75.tfm) = %{tl_version}
Provides:       tex(nanumgtb76.tfm) = %{tl_version}, tex(nanumgtb77.tfm) = %{tl_version}
Provides:       tex(nanumgtb78.tfm) = %{tl_version}, tex(nanumgtb79.tfm) = %{tl_version}
Provides:       tex(nanumgtb7a.tfm) = %{tl_version}, tex(nanumgtb7b.tfm) = %{tl_version}
Provides:       tex(nanumgtb7c.tfm) = %{tl_version}, tex(nanumgtb7d.tfm) = %{tl_version}
Provides:       tex(nanumgtb7e.tfm) = %{tl_version}, tex(nanumgtb7f.tfm) = %{tl_version}
Provides:       tex(nanumgtb80.tfm) = %{tl_version}, tex(nanumgtb81.tfm) = %{tl_version}
Provides:       tex(nanumgtb82.tfm) = %{tl_version}, tex(nanumgtb83.tfm) = %{tl_version}
Provides:       tex(nanumgtb84.tfm) = %{tl_version}, tex(nanumgtb85.tfm) = %{tl_version}
Provides:       tex(nanumgtb86.tfm) = %{tl_version}, tex(nanumgtb87.tfm) = %{tl_version}
Provides:       tex(nanumgtb88.tfm) = %{tl_version}, tex(nanumgtb89.tfm) = %{tl_version}
Provides:       tex(nanumgtb8a.tfm) = %{tl_version}, tex(nanumgtb8b.tfm) = %{tl_version}
Provides:       tex(nanumgtb8c.tfm) = %{tl_version}, tex(nanumgtb8d.tfm) = %{tl_version}
Provides:       tex(nanumgtb8e.tfm) = %{tl_version}, tex(nanumgtb8f.tfm) = %{tl_version}
Provides:       tex(nanumgtb90.tfm) = %{tl_version}, tex(nanumgtb91.tfm) = %{tl_version}
Provides:       tex(nanumgtb92.tfm) = %{tl_version}, tex(nanumgtb93.tfm) = %{tl_version}
Provides:       tex(nanumgtb94.tfm) = %{tl_version}, tex(nanumgtb95.tfm) = %{tl_version}
Provides:       tex(nanumgtb96.tfm) = %{tl_version}, tex(nanumgtb97.tfm) = %{tl_version}
Provides:       tex(nanumgtb98.tfm) = %{tl_version}, tex(nanumgtb99.tfm) = %{tl_version}
Provides:       tex(nanumgtb9a.tfm) = %{tl_version}, tex(nanumgtb9b.tfm) = %{tl_version}
Provides:       tex(nanumgtb9c.tfm) = %{tl_version}, tex(nanumgtb9d.tfm) = %{tl_version}
Provides:       tex(nanumgtb9e.tfm) = %{tl_version}, tex(nanumgtb9f.tfm) = %{tl_version}
Provides:       tex(nanumgtbac.tfm) = %{tl_version}, tex(nanumgtbad.tfm) = %{tl_version}
Provides:       tex(nanumgtbae.tfm) = %{tl_version}, tex(nanumgtbaf.tfm) = %{tl_version}
Provides:       tex(nanumgtbb0.tfm) = %{tl_version}, tex(nanumgtbb1.tfm) = %{tl_version}
Provides:       tex(nanumgtbb2.tfm) = %{tl_version}, tex(nanumgtbb3.tfm) = %{tl_version}
Provides:       tex(nanumgtbb4.tfm) = %{tl_version}, tex(nanumgtbb5.tfm) = %{tl_version}
Provides:       tex(nanumgtbb6.tfm) = %{tl_version}, tex(nanumgtbb7.tfm) = %{tl_version}
Provides:       tex(nanumgtbb8.tfm) = %{tl_version}, tex(nanumgtbb9.tfm) = %{tl_version}
Provides:       tex(nanumgtbba.tfm) = %{tl_version}, tex(nanumgtbbb.tfm) = %{tl_version}
Provides:       tex(nanumgtbbc.tfm) = %{tl_version}, tex(nanumgtbbd.tfm) = %{tl_version}
Provides:       tex(nanumgtbbe.tfm) = %{tl_version}, tex(nanumgtbbf.tfm) = %{tl_version}
Provides:       tex(nanumgtbc0.tfm) = %{tl_version}, tex(nanumgtbc1.tfm) = %{tl_version}
Provides:       tex(nanumgtbc2.tfm) = %{tl_version}, tex(nanumgtbc3.tfm) = %{tl_version}
Provides:       tex(nanumgtbc4.tfm) = %{tl_version}, tex(nanumgtbc5.tfm) = %{tl_version}
Provides:       tex(nanumgtbc6.tfm) = %{tl_version}, tex(nanumgtbc7.tfm) = %{tl_version}
Provides:       tex(nanumgtbc8.tfm) = %{tl_version}, tex(nanumgtbc9.tfm) = %{tl_version}
Provides:       tex(nanumgtbca.tfm) = %{tl_version}, tex(nanumgtbcb.tfm) = %{tl_version}
Provides:       tex(nanumgtbcc.tfm) = %{tl_version}, tex(nanumgtbcd.tfm) = %{tl_version}
Provides:       tex(nanumgtbce.tfm) = %{tl_version}, tex(nanumgtbcf.tfm) = %{tl_version}
Provides:       tex(nanumgtbd0.tfm) = %{tl_version}, tex(nanumgtbd1.tfm) = %{tl_version}
Provides:       tex(nanumgtbd2.tfm) = %{tl_version}, tex(nanumgtbd3.tfm) = %{tl_version}
Provides:       tex(nanumgtbd4.tfm) = %{tl_version}, tex(nanumgtbd5.tfm) = %{tl_version}
Provides:       tex(nanumgtbd6.tfm) = %{tl_version}, tex(nanumgtbd7.tfm) = %{tl_version}
Provides:       tex(nanumgtbf9.tfm) = %{tl_version}, tex(nanumgtbfa.tfm) = %{tl_version}
Provides:       tex(nanumgtbff.tfm) = %{tl_version}, tex(nanumgtbo00.tfm) = %{tl_version}
Provides:       tex(nanumgtbo01.tfm) = %{tl_version}, tex(nanumgtbo02.tfm) = %{tl_version}
Provides:       tex(nanumgtbo03.tfm) = %{tl_version}, tex(nanumgtbo04.tfm) = %{tl_version}
Provides:       tex(nanumgtbo11.tfm) = %{tl_version}, tex(nanumgtbo20.tfm) = %{tl_version}
Provides:       tex(nanumgtbo21.tfm) = %{tl_version}, tex(nanumgtbo22.tfm) = %{tl_version}
Provides:       tex(nanumgtbo23.tfm) = %{tl_version}, tex(nanumgtbo24.tfm) = %{tl_version}
Provides:       tex(nanumgtbo25.tfm) = %{tl_version}, tex(nanumgtbo26.tfm) = %{tl_version}
Provides:       tex(nanumgtbo27.tfm) = %{tl_version}, tex(nanumgtbo2a.tfm) = %{tl_version}
Provides:       tex(nanumgtbo30.tfm) = %{tl_version}, tex(nanumgtbo31.tfm) = %{tl_version}
Provides:       tex(nanumgtbo32.tfm) = %{tl_version}, tex(nanumgtbo33.tfm) = %{tl_version}
Provides:       tex(nanumgtbo4e.tfm) = %{tl_version}, tex(nanumgtbo4f.tfm) = %{tl_version}
Provides:       tex(nanumgtbo50.tfm) = %{tl_version}, tex(nanumgtbo51.tfm) = %{tl_version}
Provides:       tex(nanumgtbo52.tfm) = %{tl_version}, tex(nanumgtbo53.tfm) = %{tl_version}
Provides:       tex(nanumgtbo54.tfm) = %{tl_version}, tex(nanumgtbo55.tfm) = %{tl_version}
Provides:       tex(nanumgtbo56.tfm) = %{tl_version}, tex(nanumgtbo57.tfm) = %{tl_version}
Provides:       tex(nanumgtbo58.tfm) = %{tl_version}, tex(nanumgtbo59.tfm) = %{tl_version}
Provides:       tex(nanumgtbo5a.tfm) = %{tl_version}, tex(nanumgtbo5b.tfm) = %{tl_version}
Provides:       tex(nanumgtbo5c.tfm) = %{tl_version}, tex(nanumgtbo5d.tfm) = %{tl_version}
Provides:       tex(nanumgtbo5e.tfm) = %{tl_version}, tex(nanumgtbo5f.tfm) = %{tl_version}
Provides:       tex(nanumgtbo60.tfm) = %{tl_version}, tex(nanumgtbo61.tfm) = %{tl_version}
Provides:       tex(nanumgtbo62.tfm) = %{tl_version}, tex(nanumgtbo63.tfm) = %{tl_version}
Provides:       tex(nanumgtbo64.tfm) = %{tl_version}, tex(nanumgtbo65.tfm) = %{tl_version}
Provides:       tex(nanumgtbo66.tfm) = %{tl_version}, tex(nanumgtbo67.tfm) = %{tl_version}
Provides:       tex(nanumgtbo68.tfm) = %{tl_version}, tex(nanumgtbo69.tfm) = %{tl_version}
Provides:       tex(nanumgtbo6a.tfm) = %{tl_version}, tex(nanumgtbo6b.tfm) = %{tl_version}
Provides:       tex(nanumgtbo6c.tfm) = %{tl_version}, tex(nanumgtbo6d.tfm) = %{tl_version}
Provides:       tex(nanumgtbo6e.tfm) = %{tl_version}, tex(nanumgtbo6f.tfm) = %{tl_version}
Provides:       tex(nanumgtbo70.tfm) = %{tl_version}, tex(nanumgtbo71.tfm) = %{tl_version}
Provides:       tex(nanumgtbo72.tfm) = %{tl_version}, tex(nanumgtbo73.tfm) = %{tl_version}
Provides:       tex(nanumgtbo74.tfm) = %{tl_version}, tex(nanumgtbo75.tfm) = %{tl_version}
Provides:       tex(nanumgtbo76.tfm) = %{tl_version}, tex(nanumgtbo77.tfm) = %{tl_version}
Provides:       tex(nanumgtbo78.tfm) = %{tl_version}, tex(nanumgtbo79.tfm) = %{tl_version}
Provides:       tex(nanumgtbo7a.tfm) = %{tl_version}, tex(nanumgtbo7b.tfm) = %{tl_version}
Provides:       tex(nanumgtbo7c.tfm) = %{tl_version}, tex(nanumgtbo7d.tfm) = %{tl_version}
Provides:       tex(nanumgtbo7e.tfm) = %{tl_version}, tex(nanumgtbo7f.tfm) = %{tl_version}
Provides:       tex(nanumgtbo80.tfm) = %{tl_version}, tex(nanumgtbo81.tfm) = %{tl_version}
Provides:       tex(nanumgtbo82.tfm) = %{tl_version}, tex(nanumgtbo83.tfm) = %{tl_version}
Provides:       tex(nanumgtbo84.tfm) = %{tl_version}, tex(nanumgtbo85.tfm) = %{tl_version}
Provides:       tex(nanumgtbo86.tfm) = %{tl_version}, tex(nanumgtbo87.tfm) = %{tl_version}
Provides:       tex(nanumgtbo88.tfm) = %{tl_version}, tex(nanumgtbo89.tfm) = %{tl_version}
Provides:       tex(nanumgtbo8a.tfm) = %{tl_version}, tex(nanumgtbo8b.tfm) = %{tl_version}
Provides:       tex(nanumgtbo8c.tfm) = %{tl_version}, tex(nanumgtbo8d.tfm) = %{tl_version}
Provides:       tex(nanumgtbo8e.tfm) = %{tl_version}, tex(nanumgtbo8f.tfm) = %{tl_version}
Provides:       tex(nanumgtbo90.tfm) = %{tl_version}, tex(nanumgtbo91.tfm) = %{tl_version}
Provides:       tex(nanumgtbo92.tfm) = %{tl_version}, tex(nanumgtbo93.tfm) = %{tl_version}
Provides:       tex(nanumgtbo94.tfm) = %{tl_version}, tex(nanumgtbo95.tfm) = %{tl_version}
Provides:       tex(nanumgtbo96.tfm) = %{tl_version}, tex(nanumgtbo97.tfm) = %{tl_version}
Provides:       tex(nanumgtbo98.tfm) = %{tl_version}, tex(nanumgtbo99.tfm) = %{tl_version}
Provides:       tex(nanumgtbo9a.tfm) = %{tl_version}, tex(nanumgtbo9b.tfm) = %{tl_version}
Provides:       tex(nanumgtbo9c.tfm) = %{tl_version}, tex(nanumgtbo9d.tfm) = %{tl_version}
Provides:       tex(nanumgtbo9e.tfm) = %{tl_version}, tex(nanumgtbo9f.tfm) = %{tl_version}
Provides:       tex(nanumgtboac.tfm) = %{tl_version}, tex(nanumgtboad.tfm) = %{tl_version}
Provides:       tex(nanumgtboae.tfm) = %{tl_version}, tex(nanumgtboaf.tfm) = %{tl_version}
Provides:       tex(nanumgtbob0.tfm) = %{tl_version}, tex(nanumgtbob1.tfm) = %{tl_version}
Provides:       tex(nanumgtbob2.tfm) = %{tl_version}, tex(nanumgtbob3.tfm) = %{tl_version}
Provides:       tex(nanumgtbob4.tfm) = %{tl_version}, tex(nanumgtbob5.tfm) = %{tl_version}
Provides:       tex(nanumgtbob6.tfm) = %{tl_version}, tex(nanumgtbob7.tfm) = %{tl_version}
Provides:       tex(nanumgtbob8.tfm) = %{tl_version}, tex(nanumgtbob9.tfm) = %{tl_version}
Provides:       tex(nanumgtboba.tfm) = %{tl_version}, tex(nanumgtbobb.tfm) = %{tl_version}
Provides:       tex(nanumgtbobc.tfm) = %{tl_version}, tex(nanumgtbobd.tfm) = %{tl_version}
Provides:       tex(nanumgtbobe.tfm) = %{tl_version}, tex(nanumgtbobf.tfm) = %{tl_version}
Provides:       tex(nanumgtboc0.tfm) = %{tl_version}, tex(nanumgtboc1.tfm) = %{tl_version}
Provides:       tex(nanumgtboc2.tfm) = %{tl_version}, tex(nanumgtboc3.tfm) = %{tl_version}
Provides:       tex(nanumgtboc4.tfm) = %{tl_version}, tex(nanumgtboc5.tfm) = %{tl_version}
Provides:       tex(nanumgtboc6.tfm) = %{tl_version}, tex(nanumgtboc7.tfm) = %{tl_version}
Provides:       tex(nanumgtboc8.tfm) = %{tl_version}, tex(nanumgtboc9.tfm) = %{tl_version}
Provides:       tex(nanumgtboca.tfm) = %{tl_version}, tex(nanumgtbocb.tfm) = %{tl_version}
Provides:       tex(nanumgtbocc.tfm) = %{tl_version}, tex(nanumgtbocd.tfm) = %{tl_version}
Provides:       tex(nanumgtboce.tfm) = %{tl_version}, tex(nanumgtbocf.tfm) = %{tl_version}
Provides:       tex(nanumgtbod0.tfm) = %{tl_version}, tex(nanumgtbod1.tfm) = %{tl_version}
Provides:       tex(nanumgtbod2.tfm) = %{tl_version}, tex(nanumgtbod3.tfm) = %{tl_version}
Provides:       tex(nanumgtbod4.tfm) = %{tl_version}, tex(nanumgtbod5.tfm) = %{tl_version}
Provides:       tex(nanumgtbod6.tfm) = %{tl_version}, tex(nanumgtbod7.tfm) = %{tl_version}
Provides:       tex(nanumgtbof9.tfm) = %{tl_version}, tex(nanumgtbofa.tfm) = %{tl_version}
Provides:       tex(nanumgtboff.tfm) = %{tl_version}, tex(nanumgtm00.tfm) = %{tl_version}
Provides:       tex(nanumgtm01.tfm) = %{tl_version}, tex(nanumgtm02.tfm) = %{tl_version}
Provides:       tex(nanumgtm03.tfm) = %{tl_version}, tex(nanumgtm04.tfm) = %{tl_version}
Provides:       tex(nanumgtm11.tfm) = %{tl_version}, tex(nanumgtm20.tfm) = %{tl_version}
Provides:       tex(nanumgtm21.tfm) = %{tl_version}, tex(nanumgtm22.tfm) = %{tl_version}
Provides:       tex(nanumgtm23.tfm) = %{tl_version}, tex(nanumgtm24.tfm) = %{tl_version}
Provides:       tex(nanumgtm25.tfm) = %{tl_version}, tex(nanumgtm26.tfm) = %{tl_version}
Provides:       tex(nanumgtm27.tfm) = %{tl_version}, tex(nanumgtm2a.tfm) = %{tl_version}
Provides:       tex(nanumgtm30.tfm) = %{tl_version}, tex(nanumgtm31.tfm) = %{tl_version}
Provides:       tex(nanumgtm32.tfm) = %{tl_version}, tex(nanumgtm33.tfm) = %{tl_version}
Provides:       tex(nanumgtm4e.tfm) = %{tl_version}, tex(nanumgtm4f.tfm) = %{tl_version}
Provides:       tex(nanumgtm50.tfm) = %{tl_version}, tex(nanumgtm51.tfm) = %{tl_version}
Provides:       tex(nanumgtm52.tfm) = %{tl_version}, tex(nanumgtm53.tfm) = %{tl_version}
Provides:       tex(nanumgtm54.tfm) = %{tl_version}, tex(nanumgtm55.tfm) = %{tl_version}
Provides:       tex(nanumgtm56.tfm) = %{tl_version}, tex(nanumgtm57.tfm) = %{tl_version}
Provides:       tex(nanumgtm58.tfm) = %{tl_version}, tex(nanumgtm59.tfm) = %{tl_version}
Provides:       tex(nanumgtm5a.tfm) = %{tl_version}, tex(nanumgtm5b.tfm) = %{tl_version}
Provides:       tex(nanumgtm5c.tfm) = %{tl_version}, tex(nanumgtm5d.tfm) = %{tl_version}
Provides:       tex(nanumgtm5e.tfm) = %{tl_version}, tex(nanumgtm5f.tfm) = %{tl_version}
Provides:       tex(nanumgtm60.tfm) = %{tl_version}, tex(nanumgtm61.tfm) = %{tl_version}
Provides:       tex(nanumgtm62.tfm) = %{tl_version}, tex(nanumgtm63.tfm) = %{tl_version}
Provides:       tex(nanumgtm64.tfm) = %{tl_version}, tex(nanumgtm65.tfm) = %{tl_version}
Provides:       tex(nanumgtm66.tfm) = %{tl_version}, tex(nanumgtm67.tfm) = %{tl_version}
Provides:       tex(nanumgtm68.tfm) = %{tl_version}, tex(nanumgtm69.tfm) = %{tl_version}
Provides:       tex(nanumgtm6a.tfm) = %{tl_version}, tex(nanumgtm6b.tfm) = %{tl_version}
Provides:       tex(nanumgtm6c.tfm) = %{tl_version}, tex(nanumgtm6d.tfm) = %{tl_version}
Provides:       tex(nanumgtm6e.tfm) = %{tl_version}, tex(nanumgtm6f.tfm) = %{tl_version}
Provides:       tex(nanumgtm70.tfm) = %{tl_version}, tex(nanumgtm71.tfm) = %{tl_version}
Provides:       tex(nanumgtm72.tfm) = %{tl_version}, tex(nanumgtm73.tfm) = %{tl_version}
Provides:       tex(nanumgtm74.tfm) = %{tl_version}, tex(nanumgtm75.tfm) = %{tl_version}
Provides:       tex(nanumgtm76.tfm) = %{tl_version}, tex(nanumgtm77.tfm) = %{tl_version}
Provides:       tex(nanumgtm78.tfm) = %{tl_version}, tex(nanumgtm79.tfm) = %{tl_version}
Provides:       tex(nanumgtm7a.tfm) = %{tl_version}, tex(nanumgtm7b.tfm) = %{tl_version}
Provides:       tex(nanumgtm7c.tfm) = %{tl_version}, tex(nanumgtm7d.tfm) = %{tl_version}
Provides:       tex(nanumgtm7e.tfm) = %{tl_version}, tex(nanumgtm7f.tfm) = %{tl_version}
Provides:       tex(nanumgtm80.tfm) = %{tl_version}, tex(nanumgtm81.tfm) = %{tl_version}
Provides:       tex(nanumgtm82.tfm) = %{tl_version}, tex(nanumgtm83.tfm) = %{tl_version}
Provides:       tex(nanumgtm84.tfm) = %{tl_version}, tex(nanumgtm85.tfm) = %{tl_version}
Provides:       tex(nanumgtm86.tfm) = %{tl_version}, tex(nanumgtm87.tfm) = %{tl_version}
Provides:       tex(nanumgtm88.tfm) = %{tl_version}, tex(nanumgtm89.tfm) = %{tl_version}
Provides:       tex(nanumgtm8a.tfm) = %{tl_version}, tex(nanumgtm8b.tfm) = %{tl_version}
Provides:       tex(nanumgtm8c.tfm) = %{tl_version}, tex(nanumgtm8d.tfm) = %{tl_version}
Provides:       tex(nanumgtm8e.tfm) = %{tl_version}, tex(nanumgtm8f.tfm) = %{tl_version}
Provides:       tex(nanumgtm90.tfm) = %{tl_version}, tex(nanumgtm91.tfm) = %{tl_version}
Provides:       tex(nanumgtm92.tfm) = %{tl_version}, tex(nanumgtm93.tfm) = %{tl_version}
Provides:       tex(nanumgtm94.tfm) = %{tl_version}, tex(nanumgtm95.tfm) = %{tl_version}
Provides:       tex(nanumgtm96.tfm) = %{tl_version}, tex(nanumgtm97.tfm) = %{tl_version}
Provides:       tex(nanumgtm98.tfm) = %{tl_version}, tex(nanumgtm99.tfm) = %{tl_version}
Provides:       tex(nanumgtm9a.tfm) = %{tl_version}, tex(nanumgtm9b.tfm) = %{tl_version}
Provides:       tex(nanumgtm9c.tfm) = %{tl_version}, tex(nanumgtm9d.tfm) = %{tl_version}
Provides:       tex(nanumgtm9e.tfm) = %{tl_version}, tex(nanumgtm9f.tfm) = %{tl_version}
Provides:       tex(nanumgtmac.tfm) = %{tl_version}, tex(nanumgtmad.tfm) = %{tl_version}
Provides:       tex(nanumgtmae.tfm) = %{tl_version}, tex(nanumgtmaf.tfm) = %{tl_version}
Provides:       tex(nanumgtmb0.tfm) = %{tl_version}, tex(nanumgtmb1.tfm) = %{tl_version}
Provides:       tex(nanumgtmb2.tfm) = %{tl_version}, tex(nanumgtmb3.tfm) = %{tl_version}
Provides:       tex(nanumgtmb4.tfm) = %{tl_version}, tex(nanumgtmb5.tfm) = %{tl_version}
Provides:       tex(nanumgtmb6.tfm) = %{tl_version}, tex(nanumgtmb7.tfm) = %{tl_version}
Provides:       tex(nanumgtmb8.tfm) = %{tl_version}, tex(nanumgtmb9.tfm) = %{tl_version}
Provides:       tex(nanumgtmba.tfm) = %{tl_version}, tex(nanumgtmbb.tfm) = %{tl_version}
Provides:       tex(nanumgtmbc.tfm) = %{tl_version}, tex(nanumgtmbd.tfm) = %{tl_version}
Provides:       tex(nanumgtmbe.tfm) = %{tl_version}, tex(nanumgtmbf.tfm) = %{tl_version}
Provides:       tex(nanumgtmc0.tfm) = %{tl_version}, tex(nanumgtmc1.tfm) = %{tl_version}
Provides:       tex(nanumgtmc2.tfm) = %{tl_version}, tex(nanumgtmc3.tfm) = %{tl_version}
Provides:       tex(nanumgtmc4.tfm) = %{tl_version}, tex(nanumgtmc5.tfm) = %{tl_version}
Provides:       tex(nanumgtmc6.tfm) = %{tl_version}, tex(nanumgtmc7.tfm) = %{tl_version}
Provides:       tex(nanumgtmc8.tfm) = %{tl_version}, tex(nanumgtmc9.tfm) = %{tl_version}
Provides:       tex(nanumgtmca.tfm) = %{tl_version}, tex(nanumgtmcb.tfm) = %{tl_version}
Provides:       tex(nanumgtmcc.tfm) = %{tl_version}, tex(nanumgtmcd.tfm) = %{tl_version}
Provides:       tex(nanumgtmce.tfm) = %{tl_version}, tex(nanumgtmcf.tfm) = %{tl_version}
Provides:       tex(nanumgtmd0.tfm) = %{tl_version}, tex(nanumgtmd1.tfm) = %{tl_version}
Provides:       tex(nanumgtmd2.tfm) = %{tl_version}, tex(nanumgtmd3.tfm) = %{tl_version}
Provides:       tex(nanumgtmd4.tfm) = %{tl_version}, tex(nanumgtmd5.tfm) = %{tl_version}
Provides:       tex(nanumgtmd6.tfm) = %{tl_version}, tex(nanumgtmd7.tfm) = %{tl_version}
Provides:       tex(nanumgtmf9.tfm) = %{tl_version}, tex(nanumgtmfa.tfm) = %{tl_version}
Provides:       tex(nanumgtmff.tfm) = %{tl_version}, tex(nanumgtmo00.tfm) = %{tl_version}
Provides:       tex(nanumgtmo01.tfm) = %{tl_version}, tex(nanumgtmo02.tfm) = %{tl_version}
Provides:       tex(nanumgtmo03.tfm) = %{tl_version}, tex(nanumgtmo04.tfm) = %{tl_version}
Provides:       tex(nanumgtmo11.tfm) = %{tl_version}, tex(nanumgtmo20.tfm) = %{tl_version}
Provides:       tex(nanumgtmo21.tfm) = %{tl_version}, tex(nanumgtmo22.tfm) = %{tl_version}
Provides:       tex(nanumgtmo23.tfm) = %{tl_version}, tex(nanumgtmo24.tfm) = %{tl_version}
Provides:       tex(nanumgtmo25.tfm) = %{tl_version}, tex(nanumgtmo26.tfm) = %{tl_version}
Provides:       tex(nanumgtmo27.tfm) = %{tl_version}, tex(nanumgtmo2a.tfm) = %{tl_version}
Provides:       tex(nanumgtmo30.tfm) = %{tl_version}, tex(nanumgtmo31.tfm) = %{tl_version}
Provides:       tex(nanumgtmo32.tfm) = %{tl_version}, tex(nanumgtmo33.tfm) = %{tl_version}
Provides:       tex(nanumgtmo4e.tfm) = %{tl_version}, tex(nanumgtmo4f.tfm) = %{tl_version}
Provides:       tex(nanumgtmo50.tfm) = %{tl_version}, tex(nanumgtmo51.tfm) = %{tl_version}
Provides:       tex(nanumgtmo52.tfm) = %{tl_version}, tex(nanumgtmo53.tfm) = %{tl_version}
Provides:       tex(nanumgtmo54.tfm) = %{tl_version}, tex(nanumgtmo55.tfm) = %{tl_version}
Provides:       tex(nanumgtmo56.tfm) = %{tl_version}, tex(nanumgtmo57.tfm) = %{tl_version}
Provides:       tex(nanumgtmo58.tfm) = %{tl_version}, tex(nanumgtmo59.tfm) = %{tl_version}
Provides:       tex(nanumgtmo5a.tfm) = %{tl_version}, tex(nanumgtmo5b.tfm) = %{tl_version}
Provides:       tex(nanumgtmo5c.tfm) = %{tl_version}, tex(nanumgtmo5d.tfm) = %{tl_version}
Provides:       tex(nanumgtmo5e.tfm) = %{tl_version}, tex(nanumgtmo5f.tfm) = %{tl_version}
Provides:       tex(nanumgtmo60.tfm) = %{tl_version}, tex(nanumgtmo61.tfm) = %{tl_version}
Provides:       tex(nanumgtmo62.tfm) = %{tl_version}, tex(nanumgtmo63.tfm) = %{tl_version}
Provides:       tex(nanumgtmo64.tfm) = %{tl_version}, tex(nanumgtmo65.tfm) = %{tl_version}
Provides:       tex(nanumgtmo66.tfm) = %{tl_version}, tex(nanumgtmo67.tfm) = %{tl_version}
Provides:       tex(nanumgtmo68.tfm) = %{tl_version}, tex(nanumgtmo69.tfm) = %{tl_version}
Provides:       tex(nanumgtmo6a.tfm) = %{tl_version}, tex(nanumgtmo6b.tfm) = %{tl_version}
Provides:       tex(nanumgtmo6c.tfm) = %{tl_version}, tex(nanumgtmo6d.tfm) = %{tl_version}
Provides:       tex(nanumgtmo6e.tfm) = %{tl_version}, tex(nanumgtmo6f.tfm) = %{tl_version}
Provides:       tex(nanumgtmo70.tfm) = %{tl_version}, tex(nanumgtmo71.tfm) = %{tl_version}
Provides:       tex(nanumgtmo72.tfm) = %{tl_version}, tex(nanumgtmo73.tfm) = %{tl_version}
Provides:       tex(nanumgtmo74.tfm) = %{tl_version}, tex(nanumgtmo75.tfm) = %{tl_version}
Provides:       tex(nanumgtmo76.tfm) = %{tl_version}, tex(nanumgtmo77.tfm) = %{tl_version}
Provides:       tex(nanumgtmo78.tfm) = %{tl_version}, tex(nanumgtmo79.tfm) = %{tl_version}
Provides:       tex(nanumgtmo7a.tfm) = %{tl_version}, tex(nanumgtmo7b.tfm) = %{tl_version}
Provides:       tex(nanumgtmo7c.tfm) = %{tl_version}, tex(nanumgtmo7d.tfm) = %{tl_version}
Provides:       tex(nanumgtmo7e.tfm) = %{tl_version}, tex(nanumgtmo7f.tfm) = %{tl_version}
Provides:       tex(nanumgtmo80.tfm) = %{tl_version}, tex(nanumgtmo81.tfm) = %{tl_version}
Provides:       tex(nanumgtmo82.tfm) = %{tl_version}, tex(nanumgtmo83.tfm) = %{tl_version}
Provides:       tex(nanumgtmo84.tfm) = %{tl_version}, tex(nanumgtmo85.tfm) = %{tl_version}
Provides:       tex(nanumgtmo86.tfm) = %{tl_version}, tex(nanumgtmo87.tfm) = %{tl_version}
Provides:       tex(nanumgtmo88.tfm) = %{tl_version}, tex(nanumgtmo89.tfm) = %{tl_version}
Provides:       tex(nanumgtmo8a.tfm) = %{tl_version}, tex(nanumgtmo8b.tfm) = %{tl_version}
Provides:       tex(nanumgtmo8c.tfm) = %{tl_version}, tex(nanumgtmo8d.tfm) = %{tl_version}
Provides:       tex(nanumgtmo8e.tfm) = %{tl_version}, tex(nanumgtmo8f.tfm) = %{tl_version}
Provides:       tex(nanumgtmo90.tfm) = %{tl_version}, tex(nanumgtmo91.tfm) = %{tl_version}
Provides:       tex(nanumgtmo92.tfm) = %{tl_version}, tex(nanumgtmo93.tfm) = %{tl_version}
Provides:       tex(nanumgtmo94.tfm) = %{tl_version}, tex(nanumgtmo95.tfm) = %{tl_version}
Provides:       tex(nanumgtmo96.tfm) = %{tl_version}, tex(nanumgtmo97.tfm) = %{tl_version}
Provides:       tex(nanumgtmo98.tfm) = %{tl_version}, tex(nanumgtmo99.tfm) = %{tl_version}
Provides:       tex(nanumgtmo9a.tfm) = %{tl_version}, tex(nanumgtmo9b.tfm) = %{tl_version}
Provides:       tex(nanumgtmo9c.tfm) = %{tl_version}, tex(nanumgtmo9d.tfm) = %{tl_version}
Provides:       tex(nanumgtmo9e.tfm) = %{tl_version}, tex(nanumgtmo9f.tfm) = %{tl_version}
Provides:       tex(nanumgtmoac.tfm) = %{tl_version}, tex(nanumgtmoad.tfm) = %{tl_version}
Provides:       tex(nanumgtmoae.tfm) = %{tl_version}, tex(nanumgtmoaf.tfm) = %{tl_version}
Provides:       tex(nanumgtmob0.tfm) = %{tl_version}, tex(nanumgtmob1.tfm) = %{tl_version}
Provides:       tex(nanumgtmob2.tfm) = %{tl_version}, tex(nanumgtmob3.tfm) = %{tl_version}
Provides:       tex(nanumgtmob4.tfm) = %{tl_version}, tex(nanumgtmob5.tfm) = %{tl_version}
Provides:       tex(nanumgtmob6.tfm) = %{tl_version}, tex(nanumgtmob7.tfm) = %{tl_version}
Provides:       tex(nanumgtmob8.tfm) = %{tl_version}, tex(nanumgtmob9.tfm) = %{tl_version}
Provides:       tex(nanumgtmoba.tfm) = %{tl_version}, tex(nanumgtmobb.tfm) = %{tl_version}
Provides:       tex(nanumgtmobc.tfm) = %{tl_version}, tex(nanumgtmobd.tfm) = %{tl_version}
Provides:       tex(nanumgtmobe.tfm) = %{tl_version}, tex(nanumgtmobf.tfm) = %{tl_version}
Provides:       tex(nanumgtmoc0.tfm) = %{tl_version}, tex(nanumgtmoc1.tfm) = %{tl_version}
Provides:       tex(nanumgtmoc2.tfm) = %{tl_version}, tex(nanumgtmoc3.tfm) = %{tl_version}
Provides:       tex(nanumgtmoc4.tfm) = %{tl_version}, tex(nanumgtmoc5.tfm) = %{tl_version}
Provides:       tex(nanumgtmoc6.tfm) = %{tl_version}, tex(nanumgtmoc7.tfm) = %{tl_version}
Provides:       tex(nanumgtmoc8.tfm) = %{tl_version}, tex(nanumgtmoc9.tfm) = %{tl_version}
Provides:       tex(nanumgtmoca.tfm) = %{tl_version}, tex(nanumgtmocb.tfm) = %{tl_version}
Provides:       tex(nanumgtmocc.tfm) = %{tl_version}, tex(nanumgtmocd.tfm) = %{tl_version}
Provides:       tex(nanumgtmoce.tfm) = %{tl_version}, tex(nanumgtmocf.tfm) = %{tl_version}
Provides:       tex(nanumgtmod0.tfm) = %{tl_version}, tex(nanumgtmod1.tfm) = %{tl_version}
Provides:       tex(nanumgtmod2.tfm) = %{tl_version}, tex(nanumgtmod3.tfm) = %{tl_version}
Provides:       tex(nanumgtmod4.tfm) = %{tl_version}, tex(nanumgtmod5.tfm) = %{tl_version}
Provides:       tex(nanumgtmod6.tfm) = %{tl_version}, tex(nanumgtmod7.tfm) = %{tl_version}
Provides:       tex(nanumgtmof9.tfm) = %{tl_version}, tex(nanumgtmofa.tfm) = %{tl_version}
Provides:       tex(nanumgtmoff.tfm) = %{tl_version}, tex(nanummjb00.tfm) = %{tl_version}
Provides:       tex(nanummjb01.tfm) = %{tl_version}, tex(nanummjb02.tfm) = %{tl_version}
Provides:       tex(nanummjb03.tfm) = %{tl_version}, tex(nanummjb04.tfm) = %{tl_version}
Provides:       tex(nanummjb20.tfm) = %{tl_version}, tex(nanummjb21.tfm) = %{tl_version}
Provides:       tex(nanummjb22.tfm) = %{tl_version}, tex(nanummjb23.tfm) = %{tl_version}
Provides:       tex(nanummjb24.tfm) = %{tl_version}, tex(nanummjb25.tfm) = %{tl_version}
Provides:       tex(nanummjb26.tfm) = %{tl_version}, tex(nanummjb27.tfm) = %{tl_version}
Provides:       tex(nanummjb2a.tfm) = %{tl_version}, tex(nanummjb30.tfm) = %{tl_version}
Provides:       tex(nanummjb31.tfm) = %{tl_version}, tex(nanummjb32.tfm) = %{tl_version}
Provides:       tex(nanummjb33.tfm) = %{tl_version}, tex(nanummjbac.tfm) = %{tl_version}
Provides:       tex(nanummjbad.tfm) = %{tl_version}, tex(nanummjbae.tfm) = %{tl_version}
Provides:       tex(nanummjbaf.tfm) = %{tl_version}, tex(nanummjbb0.tfm) = %{tl_version}
Provides:       tex(nanummjbb1.tfm) = %{tl_version}, tex(nanummjbb2.tfm) = %{tl_version}
Provides:       tex(nanummjbb3.tfm) = %{tl_version}, tex(nanummjbb4.tfm) = %{tl_version}
Provides:       tex(nanummjbb5.tfm) = %{tl_version}, tex(nanummjbb6.tfm) = %{tl_version}
Provides:       tex(nanummjbb7.tfm) = %{tl_version}, tex(nanummjbb8.tfm) = %{tl_version}
Provides:       tex(nanummjbb9.tfm) = %{tl_version}, tex(nanummjbba.tfm) = %{tl_version}
Provides:       tex(nanummjbbb.tfm) = %{tl_version}, tex(nanummjbbc.tfm) = %{tl_version}
Provides:       tex(nanummjbbd.tfm) = %{tl_version}, tex(nanummjbbe.tfm) = %{tl_version}
Provides:       tex(nanummjbbf.tfm) = %{tl_version}, tex(nanummjbc0.tfm) = %{tl_version}
Provides:       tex(nanummjbc1.tfm) = %{tl_version}, tex(nanummjbc2.tfm) = %{tl_version}
Provides:       tex(nanummjbc3.tfm) = %{tl_version}, tex(nanummjbc4.tfm) = %{tl_version}
Provides:       tex(nanummjbc5.tfm) = %{tl_version}, tex(nanummjbc6.tfm) = %{tl_version}
Provides:       tex(nanummjbc7.tfm) = %{tl_version}, tex(nanummjbc8.tfm) = %{tl_version}
Provides:       tex(nanummjbc9.tfm) = %{tl_version}, tex(nanummjbca.tfm) = %{tl_version}
Provides:       tex(nanummjbcb.tfm) = %{tl_version}, tex(nanummjbcc.tfm) = %{tl_version}
Provides:       tex(nanummjbcd.tfm) = %{tl_version}, tex(nanummjbce.tfm) = %{tl_version}
Provides:       tex(nanummjbcf.tfm) = %{tl_version}, tex(nanummjbd0.tfm) = %{tl_version}
Provides:       tex(nanummjbd1.tfm) = %{tl_version}, tex(nanummjbd2.tfm) = %{tl_version}
Provides:       tex(nanummjbd3.tfm) = %{tl_version}, tex(nanummjbd4.tfm) = %{tl_version}
Provides:       tex(nanummjbd5.tfm) = %{tl_version}, tex(nanummjbd6.tfm) = %{tl_version}
Provides:       tex(nanummjbd7.tfm) = %{tl_version}, tex(nanummjbff.tfm) = %{tl_version}
Provides:       tex(nanummjbo00.tfm) = %{tl_version}, tex(nanummjbo01.tfm) = %{tl_version}
Provides:       tex(nanummjbo02.tfm) = %{tl_version}, tex(nanummjbo03.tfm) = %{tl_version}
Provides:       tex(nanummjbo04.tfm) = %{tl_version}, tex(nanummjbo20.tfm) = %{tl_version}
Provides:       tex(nanummjbo21.tfm) = %{tl_version}, tex(nanummjbo22.tfm) = %{tl_version}
Provides:       tex(nanummjbo23.tfm) = %{tl_version}, tex(nanummjbo24.tfm) = %{tl_version}
Provides:       tex(nanummjbo25.tfm) = %{tl_version}, tex(nanummjbo26.tfm) = %{tl_version}
Provides:       tex(nanummjbo27.tfm) = %{tl_version}, tex(nanummjbo2a.tfm) = %{tl_version}
Provides:       tex(nanummjbo30.tfm) = %{tl_version}, tex(nanummjbo31.tfm) = %{tl_version}
Provides:       tex(nanummjbo32.tfm) = %{tl_version}, tex(nanummjbo33.tfm) = %{tl_version}
Provides:       tex(nanummjboac.tfm) = %{tl_version}, tex(nanummjboad.tfm) = %{tl_version}
Provides:       tex(nanummjboae.tfm) = %{tl_version}, tex(nanummjboaf.tfm) = %{tl_version}
Provides:       tex(nanummjbob0.tfm) = %{tl_version}, tex(nanummjbob1.tfm) = %{tl_version}
Provides:       tex(nanummjbob2.tfm) = %{tl_version}, tex(nanummjbob3.tfm) = %{tl_version}
Provides:       tex(nanummjbob4.tfm) = %{tl_version}, tex(nanummjbob5.tfm) = %{tl_version}
Provides:       tex(nanummjbob6.tfm) = %{tl_version}, tex(nanummjbob7.tfm) = %{tl_version}
Provides:       tex(nanummjbob8.tfm) = %{tl_version}, tex(nanummjbob9.tfm) = %{tl_version}
Provides:       tex(nanummjboba.tfm) = %{tl_version}, tex(nanummjbobb.tfm) = %{tl_version}
Provides:       tex(nanummjbobc.tfm) = %{tl_version}, tex(nanummjbobd.tfm) = %{tl_version}
Provides:       tex(nanummjbobe.tfm) = %{tl_version}, tex(nanummjbobf.tfm) = %{tl_version}
Provides:       tex(nanummjboc0.tfm) = %{tl_version}, tex(nanummjboc1.tfm) = %{tl_version}
Provides:       tex(nanummjboc2.tfm) = %{tl_version}, tex(nanummjboc3.tfm) = %{tl_version}
Provides:       tex(nanummjboc4.tfm) = %{tl_version}, tex(nanummjboc5.tfm) = %{tl_version}
Provides:       tex(nanummjboc6.tfm) = %{tl_version}, tex(nanummjboc7.tfm) = %{tl_version}
Provides:       tex(nanummjboc8.tfm) = %{tl_version}, tex(nanummjboc9.tfm) = %{tl_version}
Provides:       tex(nanummjboca.tfm) = %{tl_version}, tex(nanummjbocb.tfm) = %{tl_version}
Provides:       tex(nanummjbocc.tfm) = %{tl_version}, tex(nanummjbocd.tfm) = %{tl_version}
Provides:       tex(nanummjboce.tfm) = %{tl_version}, tex(nanummjbocf.tfm) = %{tl_version}
Provides:       tex(nanummjbod0.tfm) = %{tl_version}, tex(nanummjbod1.tfm) = %{tl_version}
Provides:       tex(nanummjbod2.tfm) = %{tl_version}, tex(nanummjbod3.tfm) = %{tl_version}
Provides:       tex(nanummjbod4.tfm) = %{tl_version}, tex(nanummjbod5.tfm) = %{tl_version}
Provides:       tex(nanummjbod6.tfm) = %{tl_version}, tex(nanummjbod7.tfm) = %{tl_version}
Provides:       tex(nanummjboff.tfm) = %{tl_version}, tex(nanummjm00.tfm) = %{tl_version}
Provides:       tex(nanummjm01.tfm) = %{tl_version}, tex(nanummjm02.tfm) = %{tl_version}
Provides:       tex(nanummjm03.tfm) = %{tl_version}, tex(nanummjm04.tfm) = %{tl_version}
Provides:       tex(nanummjm20.tfm) = %{tl_version}, tex(nanummjm21.tfm) = %{tl_version}
Provides:       tex(nanummjm22.tfm) = %{tl_version}, tex(nanummjm23.tfm) = %{tl_version}
Provides:       tex(nanummjm24.tfm) = %{tl_version}, tex(nanummjm25.tfm) = %{tl_version}
Provides:       tex(nanummjm26.tfm) = %{tl_version}, tex(nanummjm27.tfm) = %{tl_version}
Provides:       tex(nanummjm30.tfm) = %{tl_version}, tex(nanummjm31.tfm) = %{tl_version}
Provides:       tex(nanummjm32.tfm) = %{tl_version}, tex(nanummjm33.tfm) = %{tl_version}
Provides:       tex(nanummjmac.tfm) = %{tl_version}, tex(nanummjmad.tfm) = %{tl_version}
Provides:       tex(nanummjmae.tfm) = %{tl_version}, tex(nanummjmaf.tfm) = %{tl_version}
Provides:       tex(nanummjmb0.tfm) = %{tl_version}, tex(nanummjmb1.tfm) = %{tl_version}
Provides:       tex(nanummjmb2.tfm) = %{tl_version}, tex(nanummjmb3.tfm) = %{tl_version}
Provides:       tex(nanummjmb4.tfm) = %{tl_version}, tex(nanummjmb5.tfm) = %{tl_version}
Provides:       tex(nanummjmb6.tfm) = %{tl_version}, tex(nanummjmb7.tfm) = %{tl_version}
Provides:       tex(nanummjmb8.tfm) = %{tl_version}, tex(nanummjmb9.tfm) = %{tl_version}
Provides:       tex(nanummjmba.tfm) = %{tl_version}, tex(nanummjmbb.tfm) = %{tl_version}
Provides:       tex(nanummjmbc.tfm) = %{tl_version}, tex(nanummjmbd.tfm) = %{tl_version}
Provides:       tex(nanummjmbe.tfm) = %{tl_version}, tex(nanummjmbf.tfm) = %{tl_version}
Provides:       tex(nanummjmc0.tfm) = %{tl_version}, tex(nanummjmc1.tfm) = %{tl_version}
Provides:       tex(nanummjmc2.tfm) = %{tl_version}, tex(nanummjmc3.tfm) = %{tl_version}
Provides:       tex(nanummjmc4.tfm) = %{tl_version}, tex(nanummjmc5.tfm) = %{tl_version}
Provides:       tex(nanummjmc6.tfm) = %{tl_version}, tex(nanummjmc7.tfm) = %{tl_version}
Provides:       tex(nanummjmc8.tfm) = %{tl_version}, tex(nanummjmc9.tfm) = %{tl_version}
Provides:       tex(nanummjmca.tfm) = %{tl_version}, tex(nanummjmcb.tfm) = %{tl_version}
Provides:       tex(nanummjmcc.tfm) = %{tl_version}, tex(nanummjmcd.tfm) = %{tl_version}
Provides:       tex(nanummjmce.tfm) = %{tl_version}, tex(nanummjmcf.tfm) = %{tl_version}
Provides:       tex(nanummjmd0.tfm) = %{tl_version}, tex(nanummjmd1.tfm) = %{tl_version}
Provides:       tex(nanummjmd2.tfm) = %{tl_version}, tex(nanummjmd3.tfm) = %{tl_version}
Provides:       tex(nanummjmd4.tfm) = %{tl_version}, tex(nanummjmd5.tfm) = %{tl_version}
Provides:       tex(nanummjmd6.tfm) = %{tl_version}, tex(nanummjmd7.tfm) = %{tl_version}
Provides:       tex(nanummjmff.tfm) = %{tl_version}, tex(nanummjmo00.tfm) = %{tl_version}
Provides:       tex(nanummjmo01.tfm) = %{tl_version}, tex(nanummjmo02.tfm) = %{tl_version}
Provides:       tex(nanummjmo03.tfm) = %{tl_version}, tex(nanummjmo04.tfm) = %{tl_version}
Provides:       tex(nanummjmo20.tfm) = %{tl_version}, tex(nanummjmo21.tfm) = %{tl_version}
Provides:       tex(nanummjmo22.tfm) = %{tl_version}, tex(nanummjmo23.tfm) = %{tl_version}
Provides:       tex(nanummjmo24.tfm) = %{tl_version}, tex(nanummjmo25.tfm) = %{tl_version}
Provides:       tex(nanummjmo26.tfm) = %{tl_version}, tex(nanummjmo27.tfm) = %{tl_version}
Provides:       tex(nanummjmo30.tfm) = %{tl_version}, tex(nanummjmo31.tfm) = %{tl_version}
Provides:       tex(nanummjmo32.tfm) = %{tl_version}, tex(nanummjmo33.tfm) = %{tl_version}
Provides:       tex(nanummjmoac.tfm) = %{tl_version}, tex(nanummjmoad.tfm) = %{tl_version}
Provides:       tex(nanummjmoae.tfm) = %{tl_version}, tex(nanummjmoaf.tfm) = %{tl_version}
Provides:       tex(nanummjmob0.tfm) = %{tl_version}, tex(nanummjmob1.tfm) = %{tl_version}
Provides:       tex(nanummjmob2.tfm) = %{tl_version}, tex(nanummjmob3.tfm) = %{tl_version}
Provides:       tex(nanummjmob4.tfm) = %{tl_version}, tex(nanummjmob5.tfm) = %{tl_version}
Provides:       tex(nanummjmob6.tfm) = %{tl_version}, tex(nanummjmob7.tfm) = %{tl_version}
Provides:       tex(nanummjmob8.tfm) = %{tl_version}, tex(nanummjmob9.tfm) = %{tl_version}
Provides:       tex(nanummjmoba.tfm) = %{tl_version}, tex(nanummjmobb.tfm) = %{tl_version}
Provides:       tex(nanummjmobc.tfm) = %{tl_version}, tex(nanummjmobd.tfm) = %{tl_version}
Provides:       tex(nanummjmobe.tfm) = %{tl_version}, tex(nanummjmobf.tfm) = %{tl_version}
Provides:       tex(nanummjmoc0.tfm) = %{tl_version}, tex(nanummjmoc1.tfm) = %{tl_version}
Provides:       tex(nanummjmoc2.tfm) = %{tl_version}, tex(nanummjmoc3.tfm) = %{tl_version}
Provides:       tex(nanummjmoc4.tfm) = %{tl_version}, tex(nanummjmoc5.tfm) = %{tl_version}
Provides:       tex(nanummjmoc6.tfm) = %{tl_version}, tex(nanummjmoc7.tfm) = %{tl_version}
Provides:       tex(nanummjmoc8.tfm) = %{tl_version}, tex(nanummjmoc9.tfm) = %{tl_version}
Provides:       tex(nanummjmoca.tfm) = %{tl_version}, tex(nanummjmocb.tfm) = %{tl_version}
Provides:       tex(nanummjmocc.tfm) = %{tl_version}, tex(nanummjmocd.tfm) = %{tl_version}
Provides:       tex(nanummjmoce.tfm) = %{tl_version}, tex(nanummjmocf.tfm) = %{tl_version}
Provides:       tex(nanummjmod0.tfm) = %{tl_version}, tex(nanummjmod1.tfm) = %{tl_version}
Provides:       tex(nanummjmod2.tfm) = %{tl_version}, tex(nanummjmod3.tfm) = %{tl_version}
Provides:       tex(nanummjmod4.tfm) = %{tl_version}, tex(nanummjmod5.tfm) = %{tl_version}
Provides:       tex(nanummjmod6.tfm) = %{tl_version}, tex(nanummjmod7.tfm) = %{tl_version}
Provides:       tex(nanummjmoff.tfm) = %{tl_version}, tex(t1nanumgtb.tfm) = %{tl_version}
Provides:       tex(t1nanumgtbo.tfm) = %{tl_version}, tex(t1nanumgtm.tfm) = %{tl_version}
Provides:       tex(t1nanumgtmo.tfm) = %{tl_version}, tex(t1nanummjb.tfm) = %{tl_version}
Provides:       tex(t1nanummjbo.tfm) = %{tl_version}, tex(t1nanummjm.tfm) = %{tl_version}
Provides:       tex(t1nanummjmo.tfm) = %{tl_version}, tex(ts1nanumgtb.tfm) = %{tl_version}
Provides:       tex(ts1nanumgtbo.tfm) = %{tl_version}, tex(ts1nanumgtm.tfm) = %{tl_version}
Provides:       tex(ts1nanumgtmo.tfm) = %{tl_version}, tex(ts1nanummjb.tfm) = %{tl_version}
Provides:       tex(ts1nanummjbo.tfm) = %{tl_version}, tex(ts1nanummjm.tfm) = %{tl_version}
Provides:       tex(ts1nanummjmo.tfm) = %{tl_version}, tex(nanumgtb00.pfb) = %{tl_version}
Provides:       tex(nanumgtb01.pfb) = %{tl_version}, tex(nanumgtb02.pfb) = %{tl_version}
Provides:       tex(nanumgtb03.pfb) = %{tl_version}, tex(nanumgtb04.pfb) = %{tl_version}
Provides:       tex(nanumgtb11.pfb) = %{tl_version}, tex(nanumgtb20.pfb) = %{tl_version}
Provides:       tex(nanumgtb21.pfb) = %{tl_version}, tex(nanumgtb22.pfb) = %{tl_version}
Provides:       tex(nanumgtb23.pfb) = %{tl_version}, tex(nanumgtb24.pfb) = %{tl_version}
Provides:       tex(nanumgtb25.pfb) = %{tl_version}, tex(nanumgtb26.pfb) = %{tl_version}
Provides:       tex(nanumgtb27.pfb) = %{tl_version}, tex(nanumgtb2a.pfb) = %{tl_version}
Provides:       tex(nanumgtb30.pfb) = %{tl_version}, tex(nanumgtb31.pfb) = %{tl_version}
Provides:       tex(nanumgtb32.pfb) = %{tl_version}, tex(nanumgtb33.pfb) = %{tl_version}
Provides:       tex(nanumgtb4e.pfb) = %{tl_version}, tex(nanumgtb4f.pfb) = %{tl_version}
Provides:       tex(nanumgtb50.pfb) = %{tl_version}, tex(nanumgtb51.pfb) = %{tl_version}
Provides:       tex(nanumgtb52.pfb) = %{tl_version}, tex(nanumgtb53.pfb) = %{tl_version}
Provides:       tex(nanumgtb54.pfb) = %{tl_version}, tex(nanumgtb55.pfb) = %{tl_version}
Provides:       tex(nanumgtb56.pfb) = %{tl_version}, tex(nanumgtb57.pfb) = %{tl_version}
Provides:       tex(nanumgtb58.pfb) = %{tl_version}, tex(nanumgtb59.pfb) = %{tl_version}
Provides:       tex(nanumgtb5a.pfb) = %{tl_version}, tex(nanumgtb5b.pfb) = %{tl_version}
Provides:       tex(nanumgtb5c.pfb) = %{tl_version}, tex(nanumgtb5d.pfb) = %{tl_version}
Provides:       tex(nanumgtb5e.pfb) = %{tl_version}, tex(nanumgtb5f.pfb) = %{tl_version}
Provides:       tex(nanumgtb60.pfb) = %{tl_version}, tex(nanumgtb61.pfb) = %{tl_version}
Provides:       tex(nanumgtb62.pfb) = %{tl_version}, tex(nanumgtb63.pfb) = %{tl_version}
Provides:       tex(nanumgtb64.pfb) = %{tl_version}, tex(nanumgtb65.pfb) = %{tl_version}
Provides:       tex(nanumgtb66.pfb) = %{tl_version}, tex(nanumgtb67.pfb) = %{tl_version}
Provides:       tex(nanumgtb68.pfb) = %{tl_version}, tex(nanumgtb69.pfb) = %{tl_version}
Provides:       tex(nanumgtb6a.pfb) = %{tl_version}, tex(nanumgtb6b.pfb) = %{tl_version}
Provides:       tex(nanumgtb6c.pfb) = %{tl_version}, tex(nanumgtb6d.pfb) = %{tl_version}
Provides:       tex(nanumgtb6e.pfb) = %{tl_version}, tex(nanumgtb6f.pfb) = %{tl_version}
Provides:       tex(nanumgtb70.pfb) = %{tl_version}, tex(nanumgtb71.pfb) = %{tl_version}
Provides:       tex(nanumgtb72.pfb) = %{tl_version}, tex(nanumgtb73.pfb) = %{tl_version}
Provides:       tex(nanumgtb74.pfb) = %{tl_version}, tex(nanumgtb75.pfb) = %{tl_version}
Provides:       tex(nanumgtb76.pfb) = %{tl_version}, tex(nanumgtb77.pfb) = %{tl_version}
Provides:       tex(nanumgtb78.pfb) = %{tl_version}, tex(nanumgtb79.pfb) = %{tl_version}
Provides:       tex(nanumgtb7a.pfb) = %{tl_version}, tex(nanumgtb7b.pfb) = %{tl_version}
Provides:       tex(nanumgtb7c.pfb) = %{tl_version}, tex(nanumgtb7d.pfb) = %{tl_version}
Provides:       tex(nanumgtb7e.pfb) = %{tl_version}, tex(nanumgtb7f.pfb) = %{tl_version}
Provides:       tex(nanumgtb80.pfb) = %{tl_version}, tex(nanumgtb81.pfb) = %{tl_version}
Provides:       tex(nanumgtb82.pfb) = %{tl_version}, tex(nanumgtb83.pfb) = %{tl_version}
Provides:       tex(nanumgtb84.pfb) = %{tl_version}, tex(nanumgtb85.pfb) = %{tl_version}
Provides:       tex(nanumgtb86.pfb) = %{tl_version}, tex(nanumgtb87.pfb) = %{tl_version}
Provides:       tex(nanumgtb88.pfb) = %{tl_version}, tex(nanumgtb89.pfb) = %{tl_version}
Provides:       tex(nanumgtb8a.pfb) = %{tl_version}, tex(nanumgtb8b.pfb) = %{tl_version}
Provides:       tex(nanumgtb8c.pfb) = %{tl_version}, tex(nanumgtb8d.pfb) = %{tl_version}
Provides:       tex(nanumgtb8e.pfb) = %{tl_version}, tex(nanumgtb8f.pfb) = %{tl_version}
Provides:       tex(nanumgtb90.pfb) = %{tl_version}, tex(nanumgtb91.pfb) = %{tl_version}
Provides:       tex(nanumgtb92.pfb) = %{tl_version}, tex(nanumgtb93.pfb) = %{tl_version}
Provides:       tex(nanumgtb94.pfb) = %{tl_version}, tex(nanumgtb95.pfb) = %{tl_version}
Provides:       tex(nanumgtb96.pfb) = %{tl_version}, tex(nanumgtb97.pfb) = %{tl_version}
Provides:       tex(nanumgtb98.pfb) = %{tl_version}, tex(nanumgtb99.pfb) = %{tl_version}
Provides:       tex(nanumgtb9a.pfb) = %{tl_version}, tex(nanumgtb9b.pfb) = %{tl_version}
Provides:       tex(nanumgtb9c.pfb) = %{tl_version}, tex(nanumgtb9d.pfb) = %{tl_version}
Provides:       tex(nanumgtb9e.pfb) = %{tl_version}, tex(nanumgtb9f.pfb) = %{tl_version}
Provides:       tex(nanumgtbac.pfb) = %{tl_version}, tex(nanumgtbad.pfb) = %{tl_version}
Provides:       tex(nanumgtbae.pfb) = %{tl_version}, tex(nanumgtbaf.pfb) = %{tl_version}
Provides:       tex(nanumgtbb0.pfb) = %{tl_version}, tex(nanumgtbb1.pfb) = %{tl_version}
Provides:       tex(nanumgtbb2.pfb) = %{tl_version}, tex(nanumgtbb3.pfb) = %{tl_version}
Provides:       tex(nanumgtbb4.pfb) = %{tl_version}, tex(nanumgtbb5.pfb) = %{tl_version}
Provides:       tex(nanumgtbb6.pfb) = %{tl_version}, tex(nanumgtbb7.pfb) = %{tl_version}
Provides:       tex(nanumgtbb8.pfb) = %{tl_version}, tex(nanumgtbb9.pfb) = %{tl_version}
Provides:       tex(nanumgtbba.pfb) = %{tl_version}, tex(nanumgtbbb.pfb) = %{tl_version}
Provides:       tex(nanumgtbbc.pfb) = %{tl_version}, tex(nanumgtbbd.pfb) = %{tl_version}
Provides:       tex(nanumgtbbe.pfb) = %{tl_version}, tex(nanumgtbbf.pfb) = %{tl_version}
Provides:       tex(nanumgtbc0.pfb) = %{tl_version}, tex(nanumgtbc1.pfb) = %{tl_version}
Provides:       tex(nanumgtbc2.pfb) = %{tl_version}, tex(nanumgtbc3.pfb) = %{tl_version}
Provides:       tex(nanumgtbc4.pfb) = %{tl_version}, tex(nanumgtbc5.pfb) = %{tl_version}
Provides:       tex(nanumgtbc6.pfb) = %{tl_version}, tex(nanumgtbc7.pfb) = %{tl_version}
Provides:       tex(nanumgtbc8.pfb) = %{tl_version}, tex(nanumgtbc9.pfb) = %{tl_version}
Provides:       tex(nanumgtbca.pfb) = %{tl_version}, tex(nanumgtbcb.pfb) = %{tl_version}
Provides:       tex(nanumgtbcc.pfb) = %{tl_version}, tex(nanumgtbcd.pfb) = %{tl_version}
Provides:       tex(nanumgtbce.pfb) = %{tl_version}, tex(nanumgtbcf.pfb) = %{tl_version}
Provides:       tex(nanumgtbd0.pfb) = %{tl_version}, tex(nanumgtbd1.pfb) = %{tl_version}
Provides:       tex(nanumgtbd2.pfb) = %{tl_version}, tex(nanumgtbd3.pfb) = %{tl_version}
Provides:       tex(nanumgtbd4.pfb) = %{tl_version}, tex(nanumgtbd5.pfb) = %{tl_version}
Provides:       tex(nanumgtbd6.pfb) = %{tl_version}, tex(nanumgtbd7.pfb) = %{tl_version}
Provides:       tex(nanumgtbf9.pfb) = %{tl_version}, tex(nanumgtbfa.pfb) = %{tl_version}
Provides:       tex(nanumgtbff.pfb) = %{tl_version}, tex(nanumgtm00.pfb) = %{tl_version}
Provides:       tex(nanumgtm01.pfb) = %{tl_version}, tex(nanumgtm02.pfb) = %{tl_version}
Provides:       tex(nanumgtm03.pfb) = %{tl_version}, tex(nanumgtm04.pfb) = %{tl_version}
Provides:       tex(nanumgtm11.pfb) = %{tl_version}, tex(nanumgtm20.pfb) = %{tl_version}
Provides:       tex(nanumgtm21.pfb) = %{tl_version}, tex(nanumgtm22.pfb) = %{tl_version}
Provides:       tex(nanumgtm23.pfb) = %{tl_version}, tex(nanumgtm24.pfb) = %{tl_version}
Provides:       tex(nanumgtm25.pfb) = %{tl_version}, tex(nanumgtm26.pfb) = %{tl_version}
Provides:       tex(nanumgtm27.pfb) = %{tl_version}, tex(nanumgtm2a.pfb) = %{tl_version}
Provides:       tex(nanumgtm30.pfb) = %{tl_version}, tex(nanumgtm31.pfb) = %{tl_version}
Provides:       tex(nanumgtm32.pfb) = %{tl_version}, tex(nanumgtm33.pfb) = %{tl_version}
Provides:       tex(nanumgtm4e.pfb) = %{tl_version}, tex(nanumgtm4f.pfb) = %{tl_version}
Provides:       tex(nanumgtm50.pfb) = %{tl_version}, tex(nanumgtm51.pfb) = %{tl_version}
Provides:       tex(nanumgtm52.pfb) = %{tl_version}, tex(nanumgtm53.pfb) = %{tl_version}
Provides:       tex(nanumgtm54.pfb) = %{tl_version}, tex(nanumgtm55.pfb) = %{tl_version}
Provides:       tex(nanumgtm56.pfb) = %{tl_version}, tex(nanumgtm57.pfb) = %{tl_version}
Provides:       tex(nanumgtm58.pfb) = %{tl_version}, tex(nanumgtm59.pfb) = %{tl_version}
Provides:       tex(nanumgtm5a.pfb) = %{tl_version}, tex(nanumgtm5b.pfb) = %{tl_version}
Provides:       tex(nanumgtm5c.pfb) = %{tl_version}, tex(nanumgtm5d.pfb) = %{tl_version}
Provides:       tex(nanumgtm5e.pfb) = %{tl_version}, tex(nanumgtm5f.pfb) = %{tl_version}
Provides:       tex(nanumgtm60.pfb) = %{tl_version}, tex(nanumgtm61.pfb) = %{tl_version}
Provides:       tex(nanumgtm62.pfb) = %{tl_version}, tex(nanumgtm63.pfb) = %{tl_version}
Provides:       tex(nanumgtm64.pfb) = %{tl_version}, tex(nanumgtm65.pfb) = %{tl_version}
Provides:       tex(nanumgtm66.pfb) = %{tl_version}, tex(nanumgtm67.pfb) = %{tl_version}
Provides:       tex(nanumgtm68.pfb) = %{tl_version}, tex(nanumgtm69.pfb) = %{tl_version}
Provides:       tex(nanumgtm6a.pfb) = %{tl_version}, tex(nanumgtm6b.pfb) = %{tl_version}
Provides:       tex(nanumgtm6c.pfb) = %{tl_version}, tex(nanumgtm6d.pfb) = %{tl_version}
Provides:       tex(nanumgtm6e.pfb) = %{tl_version}, tex(nanumgtm6f.pfb) = %{tl_version}
Provides:       tex(nanumgtm70.pfb) = %{tl_version}, tex(nanumgtm71.pfb) = %{tl_version}
Provides:       tex(nanumgtm72.pfb) = %{tl_version}, tex(nanumgtm73.pfb) = %{tl_version}
Provides:       tex(nanumgtm74.pfb) = %{tl_version}, tex(nanumgtm75.pfb) = %{tl_version}
Provides:       tex(nanumgtm76.pfb) = %{tl_version}, tex(nanumgtm77.pfb) = %{tl_version}
Provides:       tex(nanumgtm78.pfb) = %{tl_version}, tex(nanumgtm79.pfb) = %{tl_version}
Provides:       tex(nanumgtm7a.pfb) = %{tl_version}, tex(nanumgtm7b.pfb) = %{tl_version}
Provides:       tex(nanumgtm7c.pfb) = %{tl_version}, tex(nanumgtm7d.pfb) = %{tl_version}
Provides:       tex(nanumgtm7e.pfb) = %{tl_version}, tex(nanumgtm7f.pfb) = %{tl_version}
Provides:       tex(nanumgtm80.pfb) = %{tl_version}, tex(nanumgtm81.pfb) = %{tl_version}
Provides:       tex(nanumgtm82.pfb) = %{tl_version}, tex(nanumgtm83.pfb) = %{tl_version}
Provides:       tex(nanumgtm84.pfb) = %{tl_version}, tex(nanumgtm85.pfb) = %{tl_version}
Provides:       tex(nanumgtm86.pfb) = %{tl_version}, tex(nanumgtm87.pfb) = %{tl_version}
Provides:       tex(nanumgtm88.pfb) = %{tl_version}, tex(nanumgtm89.pfb) = %{tl_version}
Provides:       tex(nanumgtm8a.pfb) = %{tl_version}, tex(nanumgtm8b.pfb) = %{tl_version}
Provides:       tex(nanumgtm8c.pfb) = %{tl_version}, tex(nanumgtm8d.pfb) = %{tl_version}
Provides:       tex(nanumgtm8e.pfb) = %{tl_version}, tex(nanumgtm8f.pfb) = %{tl_version}
Provides:       tex(nanumgtm90.pfb) = %{tl_version}, tex(nanumgtm91.pfb) = %{tl_version}
Provides:       tex(nanumgtm92.pfb) = %{tl_version}, tex(nanumgtm93.pfb) = %{tl_version}
Provides:       tex(nanumgtm94.pfb) = %{tl_version}, tex(nanumgtm95.pfb) = %{tl_version}
Provides:       tex(nanumgtm96.pfb) = %{tl_version}, tex(nanumgtm97.pfb) = %{tl_version}
Provides:       tex(nanumgtm98.pfb) = %{tl_version}, tex(nanumgtm99.pfb) = %{tl_version}
Provides:       tex(nanumgtm9a.pfb) = %{tl_version}, tex(nanumgtm9b.pfb) = %{tl_version}
Provides:       tex(nanumgtm9c.pfb) = %{tl_version}, tex(nanumgtm9d.pfb) = %{tl_version}
Provides:       tex(nanumgtm9e.pfb) = %{tl_version}, tex(nanumgtm9f.pfb) = %{tl_version}
Provides:       tex(nanumgtmac.pfb) = %{tl_version}, tex(nanumgtmad.pfb) = %{tl_version}
Provides:       tex(nanumgtmae.pfb) = %{tl_version}, tex(nanumgtmaf.pfb) = %{tl_version}
Provides:       tex(nanumgtmb0.pfb) = %{tl_version}, tex(nanumgtmb1.pfb) = %{tl_version}
Provides:       tex(nanumgtmb2.pfb) = %{tl_version}, tex(nanumgtmb3.pfb) = %{tl_version}
Provides:       tex(nanumgtmb4.pfb) = %{tl_version}, tex(nanumgtmb5.pfb) = %{tl_version}
Provides:       tex(nanumgtmb6.pfb) = %{tl_version}, tex(nanumgtmb7.pfb) = %{tl_version}
Provides:       tex(nanumgtmb8.pfb) = %{tl_version}, tex(nanumgtmb9.pfb) = %{tl_version}
Provides:       tex(nanumgtmba.pfb) = %{tl_version}, tex(nanumgtmbb.pfb) = %{tl_version}
Provides:       tex(nanumgtmbc.pfb) = %{tl_version}, tex(nanumgtmbd.pfb) = %{tl_version}
Provides:       tex(nanumgtmbe.pfb) = %{tl_version}, tex(nanumgtmbf.pfb) = %{tl_version}
Provides:       tex(nanumgtmc0.pfb) = %{tl_version}, tex(nanumgtmc1.pfb) = %{tl_version}
Provides:       tex(nanumgtmc2.pfb) = %{tl_version}, tex(nanumgtmc3.pfb) = %{tl_version}
Provides:       tex(nanumgtmc4.pfb) = %{tl_version}, tex(nanumgtmc5.pfb) = %{tl_version}
Provides:       tex(nanumgtmc6.pfb) = %{tl_version}, tex(nanumgtmc7.pfb) = %{tl_version}
Provides:       tex(nanumgtmc8.pfb) = %{tl_version}, tex(nanumgtmc9.pfb) = %{tl_version}
Provides:       tex(nanumgtmca.pfb) = %{tl_version}, tex(nanumgtmcb.pfb) = %{tl_version}
Provides:       tex(nanumgtmcc.pfb) = %{tl_version}, tex(nanumgtmcd.pfb) = %{tl_version}
Provides:       tex(nanumgtmce.pfb) = %{tl_version}, tex(nanumgtmcf.pfb) = %{tl_version}
Provides:       tex(nanumgtmd0.pfb) = %{tl_version}, tex(nanumgtmd1.pfb) = %{tl_version}
Provides:       tex(nanumgtmd2.pfb) = %{tl_version}, tex(nanumgtmd3.pfb) = %{tl_version}
Provides:       tex(nanumgtmd4.pfb) = %{tl_version}, tex(nanumgtmd5.pfb) = %{tl_version}
Provides:       tex(nanumgtmd6.pfb) = %{tl_version}, tex(nanumgtmd7.pfb) = %{tl_version}
Provides:       tex(nanumgtmf9.pfb) = %{tl_version}, tex(nanumgtmfa.pfb) = %{tl_version}
Provides:       tex(nanumgtmff.pfb) = %{tl_version}, tex(nanummjb00.pfb) = %{tl_version}
Provides:       tex(nanummjb01.pfb) = %{tl_version}, tex(nanummjb02.pfb) = %{tl_version}
Provides:       tex(nanummjb03.pfb) = %{tl_version}, tex(nanummjb04.pfb) = %{tl_version}
Provides:       tex(nanummjb20.pfb) = %{tl_version}, tex(nanummjb21.pfb) = %{tl_version}
Provides:       tex(nanummjb22.pfb) = %{tl_version}, tex(nanummjb23.pfb) = %{tl_version}
Provides:       tex(nanummjb24.pfb) = %{tl_version}, tex(nanummjb25.pfb) = %{tl_version}
Provides:       tex(nanummjb26.pfb) = %{tl_version}, tex(nanummjb27.pfb) = %{tl_version}
Provides:       tex(nanummjb2a.pfb) = %{tl_version}, tex(nanummjb30.pfb) = %{tl_version}
Provides:       tex(nanummjb31.pfb) = %{tl_version}, tex(nanummjb32.pfb) = %{tl_version}
Provides:       tex(nanummjb33.pfb) = %{tl_version}, tex(nanummjbac.pfb) = %{tl_version}
Provides:       tex(nanummjbad.pfb) = %{tl_version}, tex(nanummjbae.pfb) = %{tl_version}
Provides:       tex(nanummjbaf.pfb) = %{tl_version}, tex(nanummjbb0.pfb) = %{tl_version}
Provides:       tex(nanummjbb1.pfb) = %{tl_version}, tex(nanummjbb2.pfb) = %{tl_version}
Provides:       tex(nanummjbb3.pfb) = %{tl_version}, tex(nanummjbb4.pfb) = %{tl_version}
Provides:       tex(nanummjbb5.pfb) = %{tl_version}, tex(nanummjbb6.pfb) = %{tl_version}
Provides:       tex(nanummjbb7.pfb) = %{tl_version}, tex(nanummjbb8.pfb) = %{tl_version}
Provides:       tex(nanummjbb9.pfb) = %{tl_version}, tex(nanummjbba.pfb) = %{tl_version}
Provides:       tex(nanummjbbb.pfb) = %{tl_version}, tex(nanummjbbc.pfb) = %{tl_version}
Provides:       tex(nanummjbbd.pfb) = %{tl_version}, tex(nanummjbbe.pfb) = %{tl_version}
Provides:       tex(nanummjbbf.pfb) = %{tl_version}, tex(nanummjbc0.pfb) = %{tl_version}
Provides:       tex(nanummjbc1.pfb) = %{tl_version}, tex(nanummjbc2.pfb) = %{tl_version}
Provides:       tex(nanummjbc3.pfb) = %{tl_version}, tex(nanummjbc4.pfb) = %{tl_version}
Provides:       tex(nanummjbc5.pfb) = %{tl_version}, tex(nanummjbc6.pfb) = %{tl_version}
Provides:       tex(nanummjbc7.pfb) = %{tl_version}, tex(nanummjbc8.pfb) = %{tl_version}
Provides:       tex(nanummjbc9.pfb) = %{tl_version}, tex(nanummjbca.pfb) = %{tl_version}
Provides:       tex(nanummjbcb.pfb) = %{tl_version}, tex(nanummjbcc.pfb) = %{tl_version}
Provides:       tex(nanummjbcd.pfb) = %{tl_version}, tex(nanummjbce.pfb) = %{tl_version}
Provides:       tex(nanummjbcf.pfb) = %{tl_version}, tex(nanummjbd0.pfb) = %{tl_version}
Provides:       tex(nanummjbd1.pfb) = %{tl_version}, tex(nanummjbd2.pfb) = %{tl_version}
Provides:       tex(nanummjbd3.pfb) = %{tl_version}, tex(nanummjbd4.pfb) = %{tl_version}
Provides:       tex(nanummjbd5.pfb) = %{tl_version}, tex(nanummjbd6.pfb) = %{tl_version}
Provides:       tex(nanummjbd7.pfb) = %{tl_version}, tex(nanummjbff.pfb) = %{tl_version}
Provides:       tex(nanummjm00.pfb) = %{tl_version}, tex(nanummjm01.pfb) = %{tl_version}
Provides:       tex(nanummjm02.pfb) = %{tl_version}, tex(nanummjm03.pfb) = %{tl_version}
Provides:       tex(nanummjm04.pfb) = %{tl_version}, tex(nanummjm20.pfb) = %{tl_version}
Provides:       tex(nanummjm21.pfb) = %{tl_version}, tex(nanummjm22.pfb) = %{tl_version}
Provides:       tex(nanummjm23.pfb) = %{tl_version}, tex(nanummjm24.pfb) = %{tl_version}
Provides:       tex(nanummjm25.pfb) = %{tl_version}, tex(nanummjm26.pfb) = %{tl_version}
Provides:       tex(nanummjm27.pfb) = %{tl_version}, tex(nanummjm30.pfb) = %{tl_version}
Provides:       tex(nanummjm31.pfb) = %{tl_version}, tex(nanummjm32.pfb) = %{tl_version}
Provides:       tex(nanummjm33.pfb) = %{tl_version}, tex(nanummjmac.pfb) = %{tl_version}
Provides:       tex(nanummjmad.pfb) = %{tl_version}, tex(nanummjmae.pfb) = %{tl_version}
Provides:       tex(nanummjmaf.pfb) = %{tl_version}, tex(nanummjmb0.pfb) = %{tl_version}
Provides:       tex(nanummjmb1.pfb) = %{tl_version}, tex(nanummjmb2.pfb) = %{tl_version}
Provides:       tex(nanummjmb3.pfb) = %{tl_version}, tex(nanummjmb4.pfb) = %{tl_version}
Provides:       tex(nanummjmb5.pfb) = %{tl_version}, tex(nanummjmb6.pfb) = %{tl_version}
Provides:       tex(nanummjmb7.pfb) = %{tl_version}, tex(nanummjmb8.pfb) = %{tl_version}
Provides:       tex(nanummjmb9.pfb) = %{tl_version}, tex(nanummjmba.pfb) = %{tl_version}
Provides:       tex(nanummjmbb.pfb) = %{tl_version}, tex(nanummjmbc.pfb) = %{tl_version}
Provides:       tex(nanummjmbd.pfb) = %{tl_version}, tex(nanummjmbe.pfb) = %{tl_version}
Provides:       tex(nanummjmbf.pfb) = %{tl_version}, tex(nanummjmc0.pfb) = %{tl_version}
Provides:       tex(nanummjmc1.pfb) = %{tl_version}, tex(nanummjmc2.pfb) = %{tl_version}
Provides:       tex(nanummjmc3.pfb) = %{tl_version}, tex(nanummjmc4.pfb) = %{tl_version}
Provides:       tex(nanummjmc5.pfb) = %{tl_version}, tex(nanummjmc6.pfb) = %{tl_version}
Provides:       tex(nanummjmc7.pfb) = %{tl_version}, tex(nanummjmc8.pfb) = %{tl_version}
Provides:       tex(nanummjmc9.pfb) = %{tl_version}, tex(nanummjmca.pfb) = %{tl_version}
Provides:       tex(nanummjmcb.pfb) = %{tl_version}, tex(nanummjmcc.pfb) = %{tl_version}
Provides:       tex(nanummjmcd.pfb) = %{tl_version}, tex(nanummjmce.pfb) = %{tl_version}
Provides:       tex(nanummjmcf.pfb) = %{tl_version}, tex(nanummjmd0.pfb) = %{tl_version}
Provides:       tex(nanummjmd1.pfb) = %{tl_version}, tex(nanummjmd2.pfb) = %{tl_version}
Provides:       tex(nanummjmd3.pfb) = %{tl_version}, tex(nanummjmd4.pfb) = %{tl_version}
Provides:       tex(nanummjmd5.pfb) = %{tl_version}, tex(nanummjmd6.pfb) = %{tl_version}
Provides:       tex(nanummjmd7.pfb) = %{tl_version}, tex(nanummjmff.pfb) = %{tl_version}
Provides:       tex(t1nanumgtb.pfb) = %{tl_version}, tex(t1nanumgtm.pfb) = %{tl_version}
Provides:       tex(t1nanummjb.pfb) = %{tl_version}, tex(t1nanummjm.pfb) = %{tl_version}
Provides:       tex(ts1nanumgtb.vf) = %{tl_version}, tex(ts1nanumgtbo.vf) = %{tl_version}
Provides:       tex(ts1nanumgtm.vf) = %{tl_version}, tex(ts1nanumgtmo.vf) = %{tl_version}
Provides:       tex(ts1nanummjb.vf) = %{tl_version}, tex(ts1nanummjbo.vf) = %{tl_version}
Provides:       tex(ts1nanummjm.vf) = %{tl_version}, tex(ts1nanummjmo.vf) = %{tl_version}
Provides:       tex(c70nanumgt.fd) = %{tl_version}, tex(c70nanummj.fd) = %{tl_version}
Provides:       tex(c70uhcmj.fd) = %{tl_version}, tex(lucnanumgt.fd) = %{tl_version}
Provides:       tex(lucnanummj.fd) = %{tl_version}, tex(t1nanumgt.fd) = %{tl_version}
Provides:       tex(t1nanummj.fd) = %{tl_version}, tex(ts1nanumgt.fd) = %{tl_version}
Provides:       tex(ts1nanummj.fd) = %{tl_version}

%description -n texlive-nanumtype1
Nanum is a unicode font designed especially for Korean-language
script. The font was designed by Sandoll Communication and
Fontrix; it includes the sans serif (gothic), serif (myeongjo),
pen script and brush script typefaces. The package provides
Type1 subfonts converted from Nanum Myeongjo (Regular and
ExtraBold) and Nanum Gothic (Regular and Bold) OTFs. C70, LUC,
T1, and TS1 font definition files are also provided. (The
package does not include OpenType/TrueType files, which are
available from Naver)

%package -n texlive-nanumtype1-doc
Summary:        Documentation for nanumtype1
Version:        svn29558.3.0

Provides:       tex-nanumtype1-doc
AutoReqProv:    No

%description -n texlive-nanumtype1-doc
Documentation for nanumtype1

%package -n texlive-mwcls
Provides:       tex-mwcls = %{tl_version}
License:        LPPL
Summary:        Polish-oriented document classes
Version:        svn44352
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(mw10.clo) = %{tl_version}, tex(mw11.clo) = %{tl_version}
Provides:       tex(mw12.clo) = %{tl_version}, tex(mwart.cls) = %{tl_version}
Provides:       tex(mwbk.cls) = %{tl_version}, tex(mwbk10.clo) = %{tl_version}
Provides:       tex(mwbk11.clo) = %{tl_version}, tex(mwbk12.clo) = %{tl_version}
Provides:       tex(mwrep.cls) = %{tl_version}

%description -n texlive-mwcls
mwcls is a set of document classes for LaTeX 2e designed with
Polish typographical tradition in mind. Classes include:
'mwart' (which is a replacement for 'article'), 'mwrep'
(replacing 'report'), and 'mwbk' (replacing 'book'). Most
features present in standard classes work with mwcls classes.
Some extensions/exceptions include: sectioning commands allow
for second optional argument (it is possible to state different
texts for running head and for TOC), new environments
'itemize*' and 'enumerate*' for lists with long items, page
styles have variants for normal, opening, closing, and blank
pages.

%package -n texlive-mwcls-doc
Summary:        Documentation for mwcls
Version:        svn44352
Provides:       tex-mwcls-doc
AutoReqProv:    No

%description -n texlive-mwcls-doc
Documentation for mwcls

%package -n texlive-ms
Provides:       tex-ms = %{tl_version}
License:        LPPL
Summary:        Various LaTeX packages by Martin Schroder
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(multicol.sty), tex(ifthen.sty), tex(scrtime.sty), tex(footmisc.sty)
Provides:       tex(count1to.sty) = %{tl_version}, tex(everysel.sty) = %{tl_version}
Provides:       tex(everyshi.sty) = %{tl_version}, tex(multitoc.sty) = %{tl_version}
Provides:       tex(prelim2e.sty) = %{tl_version}, tex(ragged2e.sty) = %{tl_version}

%description -n texlive-ms
A bundle of LaTeX packages by Martin Schroder; the collection
comprises: count1to, make use of fixed TeX counters; everysel,
set commands to execute every time a font is selected;
everyshi, set commands to execute whenever a page is shipped
out; multitoc, typeset the table of contents in multiple
columns; prelim2e, mark typeset pages as preliminary; and
ragged2e, typeset ragged text and allow hyphenation.

%package -n texlive-ms-doc
Summary:        Documentation for ms
Version:        svn42428
Provides:       tex-ms-doc
AutoReqProv:    No

%description -n texlive-ms-doc
Documentation for ms

%package -n texlive-modiagram
Provides:       tex-modiagram = %{tl_version}
License:        LPPL 1.3
Summary:        Drawing molecular orbital diagrams
Version:        svn38448

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty), tex(tikz.sty)
Requires:       tex(chemgreek.sty)
Provides:       tex(modiagram.sty) = %{tl_version}

%description -n texlive-modiagram
The package provides an environment MOdiagram and some
commands, to create molecular orbital diagrams using TikZ. For
example, the MO diagram of dihydrogen would be written as:
\begin{MOdiagram} \atom{left}{ 1s = {0;up} } \atom{right}{ 1s =
{0;up} } \molecule{ 1sMO = {1;pair, } } \end{MOdiagram} The
package also needs the l3kernel and l3packages bundles from the
LaTeX 3 experimental distribution.

%package -n texlive-modiagram-doc
Summary:        Documentation for modiagram
Version:        svn38448

Provides:       tex-modiagram-doc
AutoReqProv:    No

%description -n texlive-modiagram-doc
Documentation for modiagram

%package -n texlive-neuralnetwork
Provides:       tex-neuralnetwork = %{tl_version}
License:        GPL+
Summary:        Graph-drawing for neural networks
Version:        svn31500.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(environ.sty), tex(etoolbox.sty), tex(xkeyval.sty), tex(tikz.sty)
Requires:       tex(algorithmicx.sty), tex(mathtools.sty)
Provides:       tex(neuralnetwork.sty) = %{tl_version}

%description -n texlive-neuralnetwork
The package provides facilities for graph-drawing, with
facilities designed for neural network diagrams.

%package -n texlive-neuralnetwork-doc
Summary:        Documentation for neuralnetwork
Version:        svn31500.1.0

Provides:       tex-neuralnetwork-doc
AutoReqProv:    No

%description -n texlive-neuralnetwork-doc
Documentation for neuralnetwork

%package -n texlive-numericplots
Provides:       tex-numericplots = %{tl_version}
License:        GPLv3+
Summary:        Plot numeric data (including Matlab export) using PSTricks
Version:        svn31729.2.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(fp.sty), tex(ifthen.sty), tex(pstricks.sty)
Requires:       tex(pst-node.sty), tex(pst-plot.sty), tex(pstricks-add.sty), tex(xcolor.sty)
Requires:       tex(xkeyval.sty), tex(xkvview.sty)
Provides:       tex(NumericPlots.sty) = %{tl_version}, tex(NumericPlots_TickLabels.tex) = %{tl_version}
Provides:       tex(NumericPlots_labels.tex) = %{tl_version}
Provides:       tex(NumericPlots_legend.tex) = %{tl_version}
Provides:       tex(NumericPlots_macros.tex) = %{tl_version}
Provides:       tex(NumericPlots_styles.tex) = %{tl_version}

%description -n texlive-numericplots
Plotting numeric data is a task which has often to be done for
scientific papers. LaTeX itself provides no facilities for
drawing more than the simplest plots from supplied data. The
package will process user input, and uses PSTricks to plot the
results. The package provides Matlab functions to transform
Matlab results to plottable data.

%package -n texlive-numericplots-doc
Summary:        Documentation for numericplots
Version:        svn31729.2.0.2

Provides:       tex-numericplots-doc
AutoReqProv:    No

%description -n texlive-numericplots-doc
Documentation for numericplots

%package -n texlive-moderncv
Provides:       tex-moderncv = %{tl_version}
License:        LPPL 1.3
Summary:        A modern curriculum vitae class
Version:        svn37992.2.0.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(ifthen.sty), tex(xcolor.sty), tex(ifxetex.sty)
Requires:       tex(ifluatex.sty), tex(fontenc.sty), tex(lmodern.sty), tex(url.sty)
Requires:       tex(hyperref.sty), tex(graphicx.sty), tex(fancyhdr.sty), tex(calc.sty)
Requires:       tex(xparse.sty), tex(microtype.sty), tex(moderncvcompatibility.sty), tex(tikz.sty)
Requires:       tex(changepage.sty), tex(fontawesome.sty)
Requires:       tex(tgpagella.sty), tex(ebgaramond.sty), tex(kurier.sty)
Provides:       tex(moderncv.cls) = %{tl_version}, tex(moderncvbodyi.sty) = %{tl_version}
Provides:       tex(moderncvbodyii.sty) = %{tl_version}, tex(moderncvbodyiii.sty) = %{tl_version}
Provides:       tex(moderncvbodyiv.sty) = %{tl_version}, tex(moderncvbodyv.sty) = %{tl_version}
Provides:       tex(moderncvcollection.sty) = %{tl_version}
Provides:       tex(moderncvcolorblack.sty) = %{tl_version}
Provides:       tex(moderncvcolorblue.sty) = %{tl_version}
Provides:       tex(moderncvcolorburgundy.sty) = %{tl_version}
Provides:       tex(moderncvcolorgreen.sty) = %{tl_version}
Provides:       tex(moderncvcolorgrey.sty) = %{tl_version}
Provides:       tex(moderncvcolororange.sty) = %{tl_version}
Provides:       tex(moderncvcolorpurple.sty) = %{tl_version}
Provides:       tex(moderncvcolorred.sty) = %{tl_version}
Provides:       tex(moderncvcompatibility.sty) = %{tl_version}
Provides:       tex(moderncvdebugtools.sty) = %{tl_version}
Provides:       tex(moderncvfooti.sty) = %{tl_version}, tex(moderncvheadi.sty) = %{tl_version}
Provides:       tex(moderncvheadii.sty) = %{tl_version}, tex(moderncvheadiii.sty) = %{tl_version}
Provides:       tex(moderncvheadiv.sty) = %{tl_version}, tex(moderncvheadv.sty) = %{tl_version}
Provides:       tex(moderncvheadvi.sty) = %{tl_version}, tex(moderncviconsawesome.sty) = %{tl_version}
Provides:       tex(moderncviconsletters.sty) = %{tl_version}
Provides:       tex(moderncviconsmarvosym.sty) = %{tl_version}
Provides:       tex(moderncvstylebanking.sty) = %{tl_version}
Provides:       tex(moderncvstylecasual.sty) = %{tl_version}
Provides:       tex(moderncvstyleclassic.sty) = %{tl_version}
Provides:       tex(moderncvstyleempty.sty) = %{tl_version}
Provides:       tex(moderncvstylefancy.sty) = %{tl_version}
Provides:       tex(moderncvstyleoldstyle.sty) = %{tl_version}
Provides:       tex(tweaklist.sty) = %{tl_version}

%description -n texlive-moderncv
The class provides facilities for typesetting modern
curriculums vitae, both in a classic and in a casual style. It
is fairly customizable, allowing you to define your own style
by changing the colours, the fonts, etc. A number of templates
are provided in the distribution examples subdirectory.

%package -n texlive-moderncv-doc
Summary:        Documentation for moderncv
Version:        svn37992.2.0.0

Provides:       tex-moderncv-doc
AutoReqProv:    No

%description -n texlive-moderncv-doc
Documentation for moderncv

%package -n texlive-moderntimeline
Provides:       tex-moderntimeline = %{tl_version}
License:        LPPL 1.3
Summary:        Timelines for use with moderncv
Version:        svn38254.0.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(kvoptions.sty)
Provides:       tex(moderntimeline.sty) = %{tl_version}

%description -n texlive-moderntimeline
The package provides commands to configure and to draw time
line diagrams; such diagrams are designed to fit into
Curriculum Vitae documents written using the moderncv class.

%package -n texlive-moderntimeline-doc
Summary:        Documentation for moderntimeline
Version:        svn38254.0.9

Provides:       tex-moderntimeline-doc
AutoReqProv:    No

%description -n texlive-moderntimeline-doc
Documentation for moderntimeline

%package -n texlive-modref
Provides:       tex-modref = %{tl_version}
License:        LPPL
Summary:        Customisation of cross-references in LaTeX
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty)
Provides:       tex(modref.sty) = %{tl_version}

%description -n texlive-modref
The package contains macros which allow authors to easily
customise how cross-references appear in their document, both
in general (across all cross-references) and for particular
types of references (identified by a prefix in the reference
label), in a very generic manner.

%package -n texlive-modref-doc
Summary:        Documentation for modref
Version:        svn15878.1.0

Provides:       tex-modref-doc
AutoReqProv:    No

%description -n texlive-modref-doc
Documentation for modref

%package -n texlive-modroman
Provides:       tex-modroman = %{tl_version}
License:        LPPL
Summary:        Write numbers in lower case roman numerals
Version:        svn29803.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(etoolbox.sty)
Provides:       tex(modroman.sty) = %{tl_version}

%description -n texlive-modroman
This package provides only two macros viz. \modromannumeral
which writes the number given as argument in lower case roman
numeral with a 'j' instead of a 'i' as the final letter of
numbers greater than 1 and \modroman{MyCounter} which writes
the value of a counter in the same way. You use the first in
the same way as the TeX primitive \romannumeral and the second
as LaTeX command \roman. The default option is 'vpourv' with
which 5 is 'translated' as 'v' and option 'upourv' whith which
the same 5 is given as 'u'.

%package -n texlive-modroman-doc
Summary:        Documentation for modroman
Version:        svn29803.1

Provides:       tex-modroman-doc
AutoReqProv:    No

%description -n texlive-modroman-doc
Documentation for modroman

%package -n texlive-monofill
Provides:       tex-monofill = %{tl_version}
License:        LPPL 1.3
Summary:        Alignment of plain text
Version:        svn28140.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(monofill.sty) = %{tl_version}

%description -n texlive-monofill
The package provides horizontal alignment, as in the LaTeX
command \listfiles (or the author's longnamefilelist package).
Uses may include in-text tables, or even code listings.

%package -n texlive-monofill-doc
Summary:        Documentation for monofill
Version:        svn28140.0.2

Provides:       tex-monofill-doc
AutoReqProv:    No

%description -n texlive-monofill-doc
Documentation for monofill

%package -n texlive-moreenum
Provides:       tex-moreenum = %{tl_version}
License:        LPPL 1.3
Summary:        More enumeration options
Version:        svn24479.1.03

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(alphalph.sty), tex(enumitem.sty), tex(fmtcount.sty)
Provides:       tex(moreenum.sty) = %{tl_version}

%description -n texlive-moreenum
The package provides the following new enumerate styles: \greek
for lowercase Greek letters; \Greek for uppercase Greek
letters; \enumHex for uppercase hexadecimal enumeration;
\enumhex for lowercase hexadecimal enumeration; \enumbinary for
binary enumeration; \enumoctal for octal enumeration; \levelnth
for "1st", "2nd", "3rd" etc., with the "nth"s on the baseline;
raisenth for "1st", "2nd", "3rd" etc., with the "nth"s raised;
\nthwords for "first", "second", "third" etc.; \Nthwords for
"First", "Second", "Third" etc.; \NTHWORDS for "FIRST",
"SECOND", "THIRD" etc.; \nwords for "one", "two", "three" etc.;
\Nwords for "One", "Two", "Three" etc.; and \NWORDS for "ONE",
"TWO", "THREE" etc. Each of these works with enumitem's
"starred variant" feature. So
\begin{enumerate}[label=\enumhex*] will output a hex enumerated
list. Enumitem provides a start=0 option for starting your
enumerations at 0. The package requires amsmath, alphalph,
enumitem (of course), binhex and nth, all of which are widely
available.

%package -n texlive-moreenum-doc
Summary:        Documentation for moreenum
Version:        svn24479.1.03

Provides:       tex-moreenum-doc
AutoReqProv:    No

%description -n texlive-moreenum-doc
Documentation for moreenum

%package -n texlive-morefloats
Provides:       tex-morefloats = %{tl_version}
License:        LPPL 1.3
Summary:        Increase the number of simultaneous LaTeX floats
Version:        svn37927.1.0h

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(ifetex.sty)
Provides:       tex(morefloats.sty) = %{tl_version}

%description -n texlive-morefloats
LaTeX can, by default, only cope with 18 outstanding floats;
any more, and you get the error "too many unprocessed floats".
This package releases the limit; TeX itself imposes limits
(which are independent of the help offered by e-TeX). However,
if your floats can't be placed anywhere, extending the number
of floats merely delays the arrival of the inevitable error
message.

%package -n texlive-morefloats-doc
Summary:        Documentation for morefloats
Version:        svn37927.1.0h

Provides:       tex-morefloats-doc
AutoReqProv:    No

%description -n texlive-morefloats-doc
Documentation for morefloats

%package -n texlive-morehype
Provides:       tex-morehype = %{tl_version}
License:        LPPL 1.3
Summary:        Hypertext tools for use with LaTeX
Version:        svn38815

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fifinddo.sty), tex(dowith.sty), tex(markblog.sty), tex(langcode.sty)
Provides:       tex(blog.sty) = %{tl_version}, tex(blogdot.cfg) = %{tl_version}
Provides:       tex(blogdot.sty) = %{tl_version}, tex(blogexec.sty) = %{tl_version}
Provides:       tex(blogligs.sty) = %{tl_version}, tex(hypertoc.sty) = %{tl_version}
Provides:       tex(lnavicol.sty) = %{tl_version}, tex(markblog.sty) = %{tl_version}
Provides:       tex(texlinks.sty) = %{tl_version}

%description -n texlive-morehype
The bundle provides three packages: texlinks: shorthand macros
for TeX-related external hyperlinks with hyperref, the blog
package in the present bundle, etc; hypertoc: adjust the
presentation of coloured frames in hyperref tables of contents
(article class only); blog: fast generation of simple HTML by
expanding LaTeX macros, using the fifinddo package.

%package -n texlive-morehype-doc
Summary:        Documentation for morehype
Version:        svn38815

Provides:       tex-morehype-doc
AutoReqProv:    No

%description -n texlive-morehype-doc
Documentation for morehype

%package -n texlive-moresize
Provides:       tex-moresize = %{tl_version}
License:        LPPL
Summary:        Allows font sizes up to 35.83pt
Version:        svn17513.1.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(moresize.sty) = %{tl_version}

%description -n texlive-moresize
A package for using font sizes up to 35.88pt, for example with
the EC fonts. New commands \HUGE and \ssmall for selecting font
sizes are provided together with some options working around
current LaTeX2e shortcomings in using big font sizes. The
package also provides options for improving the typesetting of
paragraphs (or headlines) with embedded math expressions at
font sizes above 17.28pt.

%package -n texlive-moresize-doc
Summary:        Documentation for moresize
Version:        svn17513.1.9

Provides:       tex-moresize-doc
AutoReqProv:    No

%description -n texlive-moresize-doc
Documentation for moresize

%package -n texlive-moreverb
Provides:       tex-moreverb = %{tl_version}
License:        LPPL
Summary:        Extended verbatim
Version:        svn22126.2.3a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty)
Provides:       tex(moreverb.sty) = %{tl_version}

%description -n texlive-moreverb
A collection of verbatim facilities that provide line-numbered
verbatim, verbatim that obey's TAB characters, verbatim input
and verbatim output to file. The package makes use of the LaTeX
required verbatim package. The package formed from a series of
small pieces, and is somewhat unstructured. The user who looks
for thought-through verbatim facilities is advised to consider
using the fancyvrb package in place of moreverb.

%package -n texlive-moreverb-doc
Summary:        Documentation for moreverb
Version:        svn22126.2.3a

Provides:       tex-moreverb-doc
AutoReqProv:    No

%description -n texlive-moreverb-doc
Documentation for moreverb

%package -n texlive-morewrites
Provides:       tex-morewrites = %{tl_version}
License:        LPPL 1.3
Summary:        Always room for a new write stream
Version:        svn47306
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(atbegshi.sty)
Provides:       tex(morewrites.sty) = %{tl_version}, tex(primargs.sty) = %{tl_version}

%description -n texlive-morewrites
The package aims to solve the error "No room for a new \write",
which occurs when the user, or when the user's packages have
'allocated too many streams using \newwrite (TeX has a fixed
maximum number - 16 - such streams built-in to its code). The
package hooks into TeX primitive commands associated with
writing to files; it should be loaded near the beginning of the
sequence of loading packages for a document. The package uses
the l3kernel bundle.

%package -n texlive-morewrites-doc
Summary:        Documentation for morewrites
Version:        svn47306
Provides:       tex-morewrites-doc
AutoReqProv:    No

%description -n texlive-morewrites-doc
Documentation for morewrites

%package -n texlive-mparhack
Provides:       tex-mparhack = %{tl_version}
License:        GPL+
Summary:        Work around a LaTeX bug in marginpars
Version:        svn15878.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mparhack.sty) = %{tl_version}

%description -n texlive-mparhack
Works around the LaTeX bug that marginpars will sometimes come
out at the wrong margin.

%package -n texlive-mparhack-doc
Summary:        Documentation for mparhack
Version:        svn15878.1.4

Provides:       tex-mparhack-doc
AutoReqProv:    No

%description -n texlive-mparhack-doc
Documentation for mparhack

%package -n texlive-msc
Provides:       tex-msc = %{tl_version}
License:        LPPL
Summary:        Draw MSC diagrams
Version:        svn15878.1.16

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(pstricks.sty), tex(calc.sty), tex(ifthen.sty)
Requires:       tex(pst-node.sty)
Provides:       tex(msc.sty) = %{tl_version}

%description -n texlive-msc
The package should be useful to all people that prepare their
texts with LaTeX and want to draw Message Sequence Charts in
their texts. The package is not an MSC editor; it simply takes
a textual description of an MSC and draws the corresponding
MSC. The current version of the MSC macro package supports the
full MSC2000 language.

%package -n texlive-msc-doc
Summary:        Documentation for msc
Version:        svn15878.1.16

Provides:       tex-msc-doc
AutoReqProv:    No

%description -n texlive-msc-doc
Documentation for msc

%package -n texlive-msg
Provides:       tex-msg = %{tl_version}
License:        LPPL
Summary:        A package for LaTeX localisation
Version:        svn15878.0.40

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(inputenc.sty)
Provides:       tex(french_msg-msg.tex) = %{tl_version}, tex(german_msg-msg.tex) = %{tl_version}
Provides:       tex(msg-msg.tex) = %{tl_version}, tex(msg.sty) = %{tl_version}
Provides:       tex(norsk_msg-msg.tex) = %{tl_version}

%description -n texlive-msg
The package is designed to localise any document class or
package. This should be very useful for end-users who could
obtain messages in their own preferred language. It is really
easy to use by writers of other classes and packages.
Volunteers are urged to test the package, report, and even to
localise the message file to their own language. Documentation
is provided in English.

%package -n texlive-msg-doc
Summary:        Documentation for msg
Version:        svn15878.0.40

Provides:       tex-msg-doc
AutoReqProv:    No

%description -n texlive-msg-doc
Documentation for msg

%package -n texlive-mslapa
Provides:       tex-mslapa = %{tl_version}
License:        Public Domain
Summary:        Michael Landy's APA citation style
Version:        svn17514.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mslapa.sty) = %{tl_version}

%description -n texlive-mslapa
LaTeX and BibTeX style files for a respectably close
approximation to APA (American Psychological Association)
citation and reference style.

%package -n texlive-mslapa-doc
Summary:        Documentation for mslapa
Version:        svn17514.0

Provides:       tex-mslapa-doc
AutoReqProv:    No

%description -n texlive-mslapa-doc
Documentation for mslapa

%package -n texlive-mtgreek
Provides:       tex-mtgreek = %{tl_version}
License:        LPPL
Summary:        Use italic and upright greek letters with mathtime
Version:        svn17967.1.1+

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mtgreek.sty) = %{tl_version}

%description -n texlive-mtgreek
This package is an add-on to the MathTime a style to provide
TeX support for the use of the MathTime(tm) fonts (formerly
distributed by YandY, Inc.). The MathTime package has uppercase
Greek letters hardwired to be upright and only upright; this
package provides a switch to choose between the two kinds of
Greek uppercase letters.

%package -n texlive-mtgreek-doc
Summary:        Documentation for mtgreek
Version:        svn17967.1.1+

Provides:       tex-mtgreek-doc
AutoReqProv:    No

%description -n texlive-mtgreek-doc
Documentation for mtgreek

%package -n texlive-multenum
Provides:       tex-multenum = %{tl_version}
License:        LPPL
Summary:        Multi-column enumerated lists
Version:        svn21775.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(multienum.sty) = %{tl_version}

%description -n texlive-multenum
Defines an environment multienumerate, that produces an
enumerated array in which columns are vertically aligned on the
counter. The motivation was lists of answers for a text book,
where there are many rather small items; the multienumerate
environment goes some way to making such lists look neater.

%package -n texlive-multenum-doc
Summary:        Documentation for multenum
Version:        svn21775.0

Provides:       tex-multenum-doc
AutoReqProv:    No

%description -n texlive-multenum-doc
Documentation for multenum

%package -n texlive-multiaudience
Provides:       tex-multiaudience = %{tl_version}
License:        LPPL 1.3
Summary:        Several versions of output from the same source
Version:        svn38035.1.03

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(environ.sty)
Provides:       tex(multiaudience.sty) = %{tl_version}

%description -n texlive-multiaudience
This package allows to generate several versions of the same
document for different audiences.

%package -n texlive-multiaudience-doc
Summary:        Documentation for multiaudience
Version:        svn38035.1.03

Provides:       tex-multiaudience-doc
AutoReqProv:    No

%description -n texlive-multiaudience-doc
Documentation for multiaudience

%package -n texlive-multibbl
Provides:       tex-multibbl = %{tl_version}
License:        LPPL
Summary:        Multiple bibliographies
Version:        svn15878.v1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(multibbl.sty) = %{tl_version}

%description -n texlive-multibbl
The package multibbl redefines the standard bibliographic
commands so that one can generate multiple reference sections.
Each section has it own auxiliary file (for use with BibTeX)
and title.

%package -n texlive-multibbl-doc
Summary:        Documentation for multibbl
Version:        svn15878.v1.1

Provides:       tex-multibbl-doc
AutoReqProv:    No

%description -n texlive-multibbl-doc
Documentation for multibbl

%package -n texlive-multicap
Provides:       tex-multicap = %{tl_version}
License:        LPPL
Summary:        Format captions inside multicols
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(multicap.sty) = %{tl_version}

%description -n texlive-multicap
This is a package for formatting captions of column figures and
column tabular material, which cannot be standard floats in a
multicols environment. The package also provides a convenient
way to customise your captions, whether they be in multicols or
not.

%package -n texlive-multicap-doc
Summary:        Documentation for multicap
Version:        svn15878.0

Provides:       tex-multicap-doc
AutoReqProv:    No

%description -n texlive-multicap-doc
Documentation for multicap

%package -n texlive-multienv
Provides:       tex-multienv = %{tl_version}
License:        LPPL 1.3
Summary:        Multiple environments using a "key=value" syntax
Version:        svn26544.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(multienv.sty) = %{tl_version}

%description -n texlive-multienv
The package provides a multienv environment which permits easy
addition of multiple environments using a key=value syntax.
Macros to define environments using this syntax are also
provided.

%package -n texlive-multienv-doc
Summary:        Documentation for multienv
Version:        svn26544.1.0

Provides:       tex-multienv-doc
AutoReqProv:    No

%description -n texlive-multienv-doc
Documentation for multienv

%package -n texlive-multiexpand
Provides:       tex-multiexpand = %{tl_version}
License:        LPPL 1.3
Summary:        Variations on the primitive command \expandafter
Version:        svn45943
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(multiexpand.sty) = %{tl_version}

%description -n texlive-multiexpand
The package provides two user commands; one that performs
multiple expansions, and one that does multiple \expandafter
operations, in a single macro call. The package requires eTeX's
\numexpr command. The author suggests that the same effect
could be provided by use of the command variant mechanisms of
LaTeX 3 (see, for example, the interface documentation of the
experimental LaTeX 3 kernel).

%package -n texlive-multiexpand-doc
Summary:        Documentation for multiexpand
Version:        svn45943
Provides:       tex-multiexpand-doc
AutoReqProv:    No

%description -n texlive-multiexpand-doc
Documentation for multiexpand

%package -n texlive-multirow
Provides:       tex-multirow = %{tl_version}
License:        LPPL
Summary:        Create tabular cells spanning multiple rows
Version:        svn48354
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(bigdelim.sty) = %{tl_version}, tex(bigstrut.sty) = %{tl_version}
Provides:       tex(multirow.sty) = %{tl_version}

%description -n texlive-multirow
The package has a lot of flexibility, including an option for
specifying an entry at the "natural" width of its text. The
package is distributed with the bigdelim and bigstrut packages,
which can be used to advantage with \multirow cells.

%package -n texlive-multirow-doc
Summary:        Documentation for multirow
Version:        svn48354
Provides:       tex-multirow-doc
AutoReqProv:    No

%description -n texlive-multirow-doc
Documentation for multirow

%package -n texlive-mversion
Provides:       tex-mversion = %{tl_version}
License:        LPPL 1.2
Summary:        Keeping track of document versions
Version:        svn29370.1.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(mVersion.sty) = %{tl_version}

%description -n texlive-mversion
The package enables the user to keep track of different
versions of a LaTeX document. The command \version prints the
version and build numbers; each time you compile your document,
the build number is increased by one. By placing \version in
the header or footer, each page can be marked with the unique
build number describing the progress of your document.

%package -n texlive-mversion-doc
Summary:        Documentation for mversion
Version:        svn29370.1.0.1

Provides:       tex-mversion-doc
AutoReqProv:    No

%description -n texlive-mversion-doc
Documentation for mversion

%package -n texlive-mwe
Provides:       tex-mwe = %{tl_version}
License:        LPPL 1.3
Summary:        Packages and image files for MWEs
Version:        svn47194
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphicx.sty), tex(lipsum.sty), tex(blindtext.sty)
Provides:       tex(example-grid-100x100bp.tex) = %{tl_version}
Provides:       tex(example-grid-100x100pt.tex) = %{tl_version}
Provides:       tex(example-image-10x16.tex) = %{tl_version}
Provides:       tex(example-image-16x10.tex) = %{tl_version}
Provides:       tex(example-image-16x9.tex) = %{tl_version}
Provides:       tex(example-image-1x1.tex) = %{tl_version}
Provides:       tex(example-image-4x3.tex) = %{tl_version}
Provides:       tex(example-image-9x16.tex) = %{tl_version}
Provides:       tex(example-image-a.tex) = %{tl_version}
Provides:       tex(example-image-a3-landscape.tex) = %{tl_version}
Provides:       tex(example-image-a3.tex) = %{tl_version}
Provides:       tex(example-image-a4-landscape.tex) = %{tl_version}
Provides:       tex(example-image-a4.tex) = %{tl_version}
Provides:       tex(example-image-a5-landscape.tex) = %{tl_version}
Provides:       tex(example-image-a5.tex) = %{tl_version}
Provides:       tex(example-image-b.tex) = %{tl_version}
Provides:       tex(example-image-c.tex) = %{tl_version}
Provides:       tex(example-image-golden-upright.tex) = %{tl_version}
Provides:       tex(example-image-golden.tex) = %{tl_version}
Provides:       tex(example-image-letter-landscape.tex) = %{tl_version}
Provides:       tex(example-image-letter.tex) = %{tl_version}
Provides:       tex(example-image.tex) = %{tl_version}, tex(mwe.sty) = %{tl_version}

%description -n texlive-mwe
The bundle provides several files useful when creating a
minimal working example (MWE). The package itself loads a small
set of packages often used when creating MWEs. In addition, a
range of images are provided, which will be installed in the
TEXMF tree, so that they may be used in any (La)TeX document.
This allows different users to share MWEs which include image
commands, without the need to share image files or to use
replacement code.

%package -n texlive-mwe-doc
Summary:        Documentation for mwe
Version:        svn47194
Provides:       tex-mwe-doc
AutoReqProv:    No

%description -n texlive-mwe-doc
Documentation for mwe

%package -n texlive-mweights
Provides:       tex-mweights = %{tl_version}
License:        LPPL
Summary:        Support for multiple-weight font packages
Version:        svn43647
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(mweights.sty) = %{tl_version}

%description -n texlive-mweights
Many font families available for use with LaTeX are available
at multiple weights. Many Type 1-oriented support packages for
such fonts re-define the standard \mddefault or \bfdefault
macros. This can create difficulties if the weight desired for
one font family isn't available for another font family, or if
it differs from the weight desired for another font family. The
package provides a solution to these difficulties.

%package -n texlive-mweights-doc
Summary:        Documentation for mweights
Version:        svn43647
Provides:       tex-mweights-doc
AutoReqProv:    No

%description -n texlive-mweights-doc
Documentation for mweights

%package -n texlive-mycv
Provides:       tex-mycv = %{tl_version}
License:        LPPL 1.3
Summary:        A list-driven CV class, allowing TikZ decorations
Version:        svn26807.1.5.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(svn-prov.sty), tex(kvoptions.sty), tex(xstring.sty), tex(ifthen.sty)
Requires:       tex(babel.sty), tex(tikz.sty), tex(xparse.sty), tex(titlesec.sty)
Requires:       tex(fancyhdr.sty), tex(xcolor.sty), tex(calligra.sty), tex(times.sty)
Requires:       tex(pifont.sty), tex(marvosym.sty), tex(amssymb.sty), tex(hyperref.sty)
Requires:       tex(geometry.sty)
Provides:       tex(mycv.cls) = %{tl_version}, tex(mycv_base.def) = %{tl_version}
Provides:       tex(mycv_dec.sty) = %{tl_version}, tex(mycv_misc.def) = %{tl_version}
Provides:       tex(mycv_style.sty) = %{tl_version}, tex(mycv_version.def) = %{tl_version}

%description -n texlive-mycv
The class provides a set of functionality for writing
"curriculum vitae" with different layouts. The idea is that a
user can write some custom configuration directives, by means
of which is possible both to produce different c.v. layouts and
quickly switch among them. In order to process such directives,
the class uses a set of lists, provided by the package
etextools. Basic support for using TikZ decorations is also
provided.

%package -n texlive-mycv-doc
Summary:        Documentation for mycv
Version:        svn26807.1.5.6

Provides:       tex-mycv-doc
AutoReqProv:    No

%description -n texlive-mycv-doc
Documentation for mycv

%package -n texlive-mylatexformat
Provides:       tex-mylatexformat = %{tl_version}
License:        LPPL 1.3
Summary:        Build a format based on the preamble of a LaTeX file
Version:        svn21392.3.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-mylatexformat
The use of formats helps to speed up compilations: packages
which have been dumped in the format are loaded at very high
speed. This is useful when a document loads many packages
(including large packages such as pgf-TikZ). The package was
developed from the work in mylatex, and eliminates many of the
limitations and problems of that package.

%package -n texlive-mylatexformat-doc
Summary:        Documentation for mylatexformat
Version:        svn21392.3.4

Provides:       tex-mylatexformat-doc
AutoReqProv:    No

%description -n texlive-mylatexformat-doc
Documentation for mylatexformat

%package -n texlive-nag
Provides:       tex-nag = %{tl_version}
License:        LPPL
Summary:        Detecting and warning about obsolete LaTeX commands
Version:        svn24741.0.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(nag-abort.cfg) = %{tl_version}, tex(nag-experimental.cfg) = %{tl_version}
Provides:       tex(nag-l2tabu.cfg) = %{tl_version}, tex(nag-orthodox.cfg) = %{tl_version}
Provides:       tex(nag.sty) = %{tl_version}

%description -n texlive-nag
Old habits die hard. All the same, there are commands, classes
and packages which are outdated and superseded. The nag package
provides routines to warn the user about the use of such
obsolete things. As an example, we provide an extension that
detects many of the "sins" described in l2tabu.

%package -n texlive-nag-doc
Summary:        Documentation for nag
Version:        svn24741.0.7

Provides:       tex-nag-doc
AutoReqProv:    No

%description -n texlive-nag-doc
Documentation for nag

%package -n texlive-nameauth
Provides:       tex-nameauth = %{tl_version}
License:        LPPL 1.3
Summary:        Name authority mechanism for consistency in body text and index
Version:        svn43586
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etoolbox.sty), tex(trimspaces.sty), tex(suffix.sty), tex(xargs.sty)
Provides:       tex(nameauth.sty) = %{tl_version}

%description -n texlive-nameauth
Publications, that reference many names, require editors and
proofreaders to track those names in the text and index. The
package offers name authority macros that allow authors and
compilers to normalize occurrences of names, variant name
forms, and pen names in the text and index. This may help
minimize writing and production time and cost.

%package -n texlive-nameauth-doc
Summary:        Documentation for nameauth
Version:        svn43586
Provides:       tex-nameauth-doc
AutoReqProv:    No

%description -n texlive-nameauth-doc
Documentation for nameauth

%package -n texlive-namespc
Provides:       tex-namespc = %{tl_version}
License:        LPPL
Summary:        Rudimentary C++-like namespaces in LaTeX
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(namespc.sty) = %{tl_version}

%description -n texlive-namespc
The namespc package adds rudimentary C++-like namespace
functionality to LaTeX. It may be used to declare local LaTeX
commands, which can be made accessible in a later contexts
without defining them globally.

%package -n texlive-namespc-doc
Summary:        Documentation for namespc
Version:        svn15878.0

Provides:       tex-namespc-doc
AutoReqProv:    No

%description -n texlive-namespc-doc
Documentation for namespc

%package -n texlive-ncclatex
Provides:       tex-ncclatex = %{tl_version}
License:        LPPL
Summary:        An extended general-purpose class
Version:        svn15878.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(afterpackage.sty), tex(tocenter.sty)
Requires:       tex(dcounter.sty), tex(makeidx.sty), tex(topsection.sty), tex(watermark.sty)
Requires:       tex(nccheadings.sty), tex(nccbiblist.sty)
Requires:       tex(nccfancyhdr.sty), tex(multicol.sty), tex(desclist.sty), tex(extdash.sty)
Requires:       tex(nccmath.sty), tex(nccsect.sty), tex(nccthm.sty), tex(nccboxes.sty)
Requires:       tex(nccfoots.sty), tex(nccpic.sty), tex(nccfloats.sty), tex(fontenc.sty)
Requires:       tex(babel.sty), tex(amstext.sty), tex(textarea.sty)
Provides:       tex(cp1251-light.def) = %{tl_version}, tex(ncc.cls) = %{tl_version}
Provides:       tex(ncc10.clo) = %{tl_version}, tex(ncc11.clo) = %{tl_version}
Provides:       tex(ncc12.clo) = %{tl_version}, tex(ncc14.clo) = %{tl_version}
Provides:       tex(nccart.clo) = %{tl_version}, tex(nccbiblist.sty) = %{tl_version}
Provides:       tex(nccbook.clo) = %{tl_version}, tex(nccdefaults.sty) = %{tl_version}
Provides:       tex(nccfit.clo) = %{tl_version}, tex(ncchdr.sty) = %{tl_version}
Provides:       tex(nccheadings.sty) = %{tl_version}, tex(nccindex.sty) = %{tl_version}
Provides:       tex(ncclatex.sty) = %{tl_version}, tex(nccltrus.sty) = %{tl_version}
Provides:       tex(nccold.sty) = %{tl_version}, tex(nccproc.cls) = %{tl_version}
Provides:       tex(nccsections.sty) = %{tl_version}, tex(ncctheorems.sty) = %{tl_version}
Provides:       tex(ncctitle.clo) = %{tl_version}, tex(ncctitle.sty) = %{tl_version}
Provides:       tex(ncctitlepage.sty) = %{tl_version}, tex(sibjnm.cls) = %{tl_version}

%description -n texlive-ncclatex
The ncc class provides a framework for a common class to
replace the standard article, book and report classes, and
providing a "preprint" class. The class's extensions are
provided in a number of small packages, some of which may also
be used with the standard classes. The ncclatex package also
loads many of the packages of, and requires the latest version
of the ncctools bundle.

%package -n texlive-ncclatex-doc
Summary:        Documentation for ncclatex
Version:        svn15878.1.5

Provides:       tex-ncclatex-doc
AutoReqProv:    No

%description -n texlive-ncclatex-doc
Documentation for ncclatex

%package -n texlive-needspace
Provides:       tex-needspace = %{tl_version}
License:        LPPL
Summary:        Insert pagebreak if not enough space
Version:        svn29601.1.3d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(needspace.sty) = %{tl_version}

%description -n texlive-needspace
Provides commands to disable pagebreaking within a given
vertical space. If there is not enough space between the
command and the bottom of the page, a new page will be started.

%package -n texlive-needspace-doc
Summary:        Documentation for needspace
Version:        svn29601.1.3d

Provides:       tex-needspace-doc
AutoReqProv:    No

%description -n texlive-needspace-doc
Documentation for needspace

%package -n texlive-nestquot
Provides:       tex-nestquot = %{tl_version}
License:        BSD
Summary:        Alternate quotes between double and single with nesting
Version:        svn27323.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(nestquot.sty) = %{tl_version}

%description -n texlive-nestquot
Provides two new commands: \nlq and \nrq for nesting left and
right quotes that properly change between double and single
quotes according to their nesting level. For example, the input
\nlq Foo \nlq bar\nrq\ bletch\nrq will be typeset as if it had
been entered as "Foo 'bar' bletch".

%package -n texlive-newcommand-doc
Summary:        Documentation for newcommand
Version:        svn18704.2.0

Provides:       tex-newcommand-doc
AutoReqProv:    No

%description -n texlive-newcommand-doc
Documentation for newcommand

%package -n texlive-newenviron
Provides:       tex-newenviron = %{tl_version}
License:        LPPL 1.3
Summary:        Processing an environment's body
Version:        svn29331.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(catoptions.sty)
Provides:       tex(newenviron.sty) = %{tl_version}

%description -n texlive-newenviron
The package offers tools for collecting and executing an
environment's body.

%package -n texlive-newenviron-doc
Summary:        Documentation for newenviron
Version:        svn29331.1.0

Provides:       tex-newenviron-doc
AutoReqProv:    No

%description -n texlive-newenviron-doc
Documentation for newenviron

%package -n texlive-newfile
Provides:       tex-newfile = %{tl_version}
License:        LPPL
Summary:        User level management of LaTeX input and output
Version:        svn15878.1.0c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty)
Provides:       tex(newfile.sty) = %{tl_version}

%description -n texlive-newfile
Commands are defined to manage the limited pool of input and
output handles provided by TeX. The streams so provided are
mapped to various of the LaTeX input and output mechanisms.
Some facilities of the verbatim package are also mapped.

%package -n texlive-newfile-doc
Summary:        Documentation for newfile
Version:        svn15878.1.0c

Provides:       tex-newfile-doc
AutoReqProv:    No

%description -n texlive-newfile-doc
Documentation for newfile

%package -n texlive-newlfm
Provides:       tex-newlfm = %{tl_version}
License:        GPL+
Summary:        Write letters, facsimiles, and memos
Version:        svn15878.9.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(ifthen.sty), tex(ifpdf.sty), tex(fancyhdr.sty)
Requires:       tex(eso-pic.sty), tex(setspace.sty), tex(lastpage.sty), tex(calc.sty)
Requires:       tex(graphicx.sty), tex(rotating.sty), tex(afterpage.sty), tex(envlab.sty)
Provides:       tex(addrset.sty) = %{tl_version}, tex(newlfm.cls) = %{tl_version}
Provides:       tex(setdim.sty) = %{tl_version}

%description -n texlive-newlfm
Integrates the letter class with fancyhdr and geometry to
automatically make letterhead stationery. Useful for writing
letters, fax, and memos. You can set up an address book using
'wrapper' macros. You put all the information for a person into
a wrapper and then put the wrapper in a document. The class
handles letterheads automatically. You place the object for the
letterhead (picture, information, etc.) in a box and all sizing
is set automatically.

%package -n texlive-newlfm-doc
Summary:        Documentation for newlfm
Version:        svn15878.9.4

Provides:       tex-newlfm-doc
AutoReqProv:    No

%description -n texlive-newlfm-doc
Documentation for newlfm

%package -n texlive-newspaper
Provides:       tex-newspaper = %{tl_version}
License:        LPPL
Summary:        Typeset newsletters to resemble newspapers
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(yfonts.sty)
Provides:       tex(newspaper.sty) = %{tl_version}

%description -n texlive-newspaper
The newspaper package redefines the page style and \maketitle
command to produce a typeset page similar to that of a
newspaper. It also provides several commands that (when used
with other packages) simplify the writing of articles in a
newspaper-style column format.

%package -n texlive-newspaper-doc
Summary:        Documentation for newspaper
Version:        svn15878.1.0

Provides:       tex-newspaper-doc
AutoReqProv:    No

%description -n texlive-newspaper-doc
Documentation for newspaper

%package -n texlive-newunicodechar
Provides:       tex-newunicodechar = %{tl_version}
License:        LPPL 1.3
Summary:        Definitions of the meaning of Unicode characters
Version:        svn47382
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(newunicodechar.sty) = %{tl_version}

%description -n texlive-newunicodechar
The package provides a friendly interface for defining the
meaning of Unicode characters. The document should be processed
by (pdf)LaTeX with the unicode option of inputenc or inputenx,
or by XeLaTeX/LuaLaTeX. The command provided is
\newunicodechar{<char>}{<code>} where <char> is a directly-
typed Unicode character, and <code> is its replacement.

%package -n texlive-newunicodechar-doc
Summary:        Documentation for newunicodechar
Version:        svn47382
Provides:       tex-newunicodechar-doc
AutoReqProv:    No

%description -n texlive-newunicodechar-doc
Documentation for newunicodechar

%package -n texlive-newvbtm
Provides:       tex-newvbtm = %{tl_version}
License:        LPPL
Summary:        Define your own verbatim-like environment
Version:        svn23996.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(newvbtm.sty) = %{tl_version}, tex(varvbtm.sty) = %{tl_version}

%description -n texlive-newvbtm
Defines general purpose macro named \newverbatim to define your
own verbatim-like environment. It also has a supplementary
style file varvbtm.sty to provide set of macros for variants of
verbatim, such as tab emulation.

%package -n texlive-newvbtm-doc
Summary:        Documentation for newvbtm
Version:        svn23996.1.1

Provides:       tex-newvbtm-doc
AutoReqProv:    No

%description -n texlive-newvbtm-doc
Documentation for newvbtm

%package -n texlive-newverbs
Provides:       tex-newverbs = %{tl_version}
License:        LPPL 1.3
Summary:        Define new versions of \verb, including short verb versions
Version:        svn26258.1.3a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(newverbs.sty) = %{tl_version}

%description -n texlive-newverbs
The package allows the definition of \verb variants which add
TeX code before and after the verbatim text (e.g., quotes or
surrounding \fbox{}). When used together with the shortvrb
package it allows the definition of short verbatim characters
which use this package's variant instead of the normal \verb.
In addition, it is possible to collect an argument verbatim to
either typeset or write it into a file. The \Verbdef command
defines verbatim text to a macro which can later be used to
write the verbatim text to a file.

%package -n texlive-newverbs-doc
Summary:        Documentation for newverbs
Version:        svn26258.1.3a

Provides:       tex-newverbs-doc
AutoReqProv:    No

%description -n texlive-newverbs-doc
Documentation for newverbs

%package -n texlive-nextpage
Provides:       tex-nextpage = %{tl_version}
License:        LPPL
Summary:        Generalisations of the page advance commands
Version:        svn15878.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(nextpage.sty) = %{tl_version}

%description -n texlive-nextpage
Provides \clearpage and \newpage variants that guarantee to end
up on even/odd numbered pages; these 4 commands all have an
optional argument whose content will be placed on any "empty"
page generated.

%package -n texlive-nfssext-cfr
Provides:       tex-nfssext-cfr = %{tl_version}
License:        LPPL 1.3
Summary:        Extensions to the LaTeX NFSS
Version:        svn43640
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(nfssext-cfr.sty) = %{tl_version}

%description -n texlive-nfssext-cfr
The package is a development of nfssext.sty, distributed with
the examples for the font installation guide. The package has
been developed for use in packages such as cfr-lm and
venturisadf,

%package -n texlive-nfssext-cfr-doc
Summary:        Documentation for nfssext-cfr
Version:        svn43640
Provides:       tex-nfssext-cfr-doc
AutoReqProv:    No

%description -n texlive-nfssext-cfr-doc
Documentation for nfssext-cfr

%package -n texlive-nicefilelist
Provides:       tex-nicefilelist = %{tl_version}
License:        LPPL 1.3
Summary:        Provide \listfiles alignment
Version:        svn28527.0.7a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(monofill.sty), tex(hardwrap.sty), tex(myfilist.sty)
Provides:       tex(nicefilelist.sty) = %{tl_version}

%description -n texlive-nicefilelist
The package extends longnamefilelist, keeping separate columns
for date, version and "caption" (the caption now separately
listed). Alignment is not disturbed by short file name
extensions, such as ".fd". The package is not compatible with
longnamefilelist: users need to re-read the documentation.

%package -n texlive-nicefilelist-doc
Summary:        Documentation for nicefilelist
Version:        svn28527.0.7a

Provides:       tex-nicefilelist-doc
AutoReqProv:    No

%description -n texlive-nicefilelist-doc
Documentation for nicefilelist

%package -n texlive-niceframe
Provides:       tex-niceframe = %{tl_version}
License:        LPPL
Summary:        Support for fancy frames
Version:        svn36086.1.1c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty)
Provides:       tex(karta15.tfm) = %{tl_version}, tex(umranda.tfm) = %{tl_version}
Provides:       tex(umrandb.tfm) = %{tl_version}, tex(niceframe.sty) = %{tl_version}

%description -n texlive-niceframe
The package defines means of drawing frames around boxes, using
dingbat fonts. Some (Metafont) font sources are included; the
fonts are available separately in Type 1 format.

%package -n texlive-niceframe-doc
Summary:        Documentation for niceframe
Version:        svn36086.1.1c

Provides:       tex-niceframe-doc
AutoReqProv:    No

%description -n texlive-niceframe-doc
Documentation for niceframe

%package -n texlive-nicetext
Provides:       tex-nicetext = %{tl_version}
License:        LPPL
Summary:        Minimal markup for simple text (Wikipedia style) and documentation
Version:        svn38914

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(stacklet.sty), tex(actcodes.sty), tex(moreverb.sty)
Provides:       tex(fifinddo.sty) = %{tl_version}, tex(makedoc.cfg) = %{tl_version}
Provides:       tex(makedoc.sty) = %{tl_version}, tex(mdoccorr.cfg) = %{tl_version}
Provides:       tex(niceverb.sty) = %{tl_version}, tex(arseneau.tex) = %{tl_version}
Provides:       tex(atari.cfg) = %{tl_version}, tex(copyfile.cfg) = %{tl_version}
Provides:       tex(copyfile.tex) = %{tl_version}, tex(fddial0g.sty) = %{tl_version}
Provides:       tex(fdtxttex.cfg) = %{tl_version}, tex(fdtxttex.tex) = %{tl_version}
Provides:       tex(substr.tex) = %{tl_version}, tex(wiki.sty) = %{tl_version}

%description -n texlive-nicetext
The bundle offers "minimal" markup syntax for various simple
kinds of text. The user will typically involve little more than
is printed, and will still get LaTeX quality. The bundle
provides four packages: wiki addresses general texts, marked up
in the simple style used on Wikipedia; niceverb is yet another
means of documenting LaTeX packages: it offers syntax-aware
typesetting of meta-variables (macro arguments) and for
referring to commands (and their syntax) in footnotes, section
titles etc.; fifinddo aims to parse plain text or (La)TeX files
using TeX, and to write the results to an external file; the
package is used by another member of the bundle: makedoc, which
provides the means to produce typeset documentation direct from
package files.

%package -n texlive-nicetext-doc
Summary:        Documentation for nicetext
Version:        svn38914

Provides:       tex-nicetext-doc
AutoReqProv:    No

%description -n texlive-nicetext-doc
Documentation for nicetext

%package -n texlive-nlctdoc
Provides:       tex-nlctdoc = %{tl_version}
License:        LPPL
Summary:        Package documentation class
Version:        svn44353
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifpdf.sty), tex(xcolor.sty), tex(inputenc.sty), tex(fontenc.sty)
Requires:       tex(cmap.sty), tex(fourier.sty), tex(tex4ht.sty), tex(etoolbox.sty)
Requires:       tex(multicol.sty), tex(dox.sty)
Provides:       tex(nlctdoc.cls) = %{tl_version}

%description -n texlive-nlctdoc
The class provides support for the documentation of the
author's packages, using koma-script. This class is provided
"as is" solely for the benefit of anyone who wants to compile
the documentation of those packages.

%package -n texlive-nlctdoc-doc
Summary:        Documentation for nlctdoc
Version:        svn44353
Provides:       tex-nlctdoc-doc
AutoReqProv:    No

%description -n texlive-nlctdoc-doc
Documentation for nlctdoc

%package -n texlive-multiobjective
Provides:       tex-multiobjective = %{tl_version}
License:        LPPL
Summary:        Symbols for multiobjective optimisation etc
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amssymb.sty)
Provides:       tex(multiobjective.sty) = %{tl_version}

%description -n texlive-multiobjective
The package provides a series of operators commonly used in
papers related to multiobjective optimisation, multiobjective
evolutionary algorithms, multicriteria decision making and
similar fields.

%package -n texlive-multiobjective-doc
Summary:        Documentation for multiobjective
Version:        svn15878.1.0

Provides:       tex-multiobjective-doc
AutoReqProv:    No

%description -n texlive-multiobjective-doc
Documentation for multiobjective

%package -n texlive-natded
Provides:       tex-natded = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset natural deduction proofs
Version:        svn32693.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(natded.sty) = %{tl_version}

%description -n texlive-natded
The package provides commands to typeset proofs in the style
used by Jaskowski, or that of Kalish and Montague.

%package -n texlive-natded-doc
Summary:        Documentation for natded
Version:        svn32693.0.1

Provides:       tex-natded-doc
AutoReqProv:    No

%description -n texlive-natded-doc
Documentation for natded

%package -n texlive-nath
Provides:       tex-nath = %{tl_version}
License:        GPL+
Summary:        Natural mathematics notation
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(nath.sty) = %{tl_version}

%description -n texlive-nath
Nath is a LaTeX (both 2e and 2.09) style to separate
presentation and content in mathematical typography. The style
delivers a particular context-dependent presentation on the
basis of a rather coarse context-independent notation.
Highlighted features: depending on the context, the command
\frac produces either built-up or case or solidus fractions,
with parentheses added whenever required for preservation of
the mathematical meaning; delimiters adapt their size to the
material enclosed, rendering \left and \right almost obsolete.

%package -n texlive-nath-doc
Summary:        Documentation for nath
Version:        svn15878.0

Provides:       tex-nath-doc
AutoReqProv:    No

%description -n texlive-nath-doc
Documentation for nath

%package -n texlive-mp3d
Provides:       tex-mp3d = %{tl_version}
License:        LPPL
Summary:        3D animations
Version:        svn29349.1.34

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-mp3d
Create animations of 3-dimensional objects (such as polyhedra)
in MetaPost.

%package -n texlive-mp3d-doc
Summary:        Documentation for mp3d
Version:        svn29349.1.34

Provides:       tex-mp3d-doc
AutoReqProv:    No

%description -n texlive-mp3d-doc
Documentation for mp3d

%package -n texlive-mpcolornames
Provides:       tex-mpcolornames = %{tl_version}
License:        LPPL
Summary:        Extend list of predefined colour names for MetaPost
Version:        svn23252.0.20

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-mpcolornames
The MetaPost format plain.mp provides only five built-in colour
names (variables), all of which are defined in the RGB model:
red, green and blue for the primary colours and black and
white. The package makes more than 500 colour names from
different colour sets in different colour models available to
MetaPost. Colour sets include X11, SVG, DVIPS and xcolor
specifications.

%package -n texlive-mpcolornames-doc
Summary:        Documentation for mpcolornames
Version:        svn23252.0.20

Provides:       tex-mpcolornames-doc
AutoReqProv:    No

%description -n texlive-mpcolornames-doc
Documentation for mpcolornames

%package -n texlive-mpattern
Provides:       tex-mpattern = %{tl_version}
License:        Public Domain
Summary:        Patterns in MetaPost
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-mpattern
A package for defining and using patterns in MetaPost, using
the Pattern Color Space available in PostScript Level 2.

%package -n texlive-mpattern-doc
Summary:        Documentation for mpattern
Version:        svn15878.0

Provides:       tex-mpattern-doc
AutoReqProv:    No

%description -n texlive-mpattern-doc
Documentation for mpattern

%package -n texlive-mpgraphics
Provides:       tex-mpgraphics = %{tl_version}
License:        LPPL 1.3
Summary:        Process and display MetaPost figures inline
Version:        svn29776.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(color.sty), tex(moreverb.sty), tex(xkeyval.sty)
Requires:       tex(ifplatform.sty), tex(iftex.sty), tex(ifpdf.sty)
Provides:       tex(mpgraphics.sty) = %{tl_version}

%description -n texlive-mpgraphics
The package allows LaTeX users to typeset MetaPost code inline
and display figures in their documents with only and only one
run of LaTeX, PDFLaTeX or XelaTeX (no separate runs of mpost).
Mpgraphics achieves this by using the shell escape (\write 18)
feature of current TeX distributions, so that the whole process
is automatic and the end user is saved the tiresome processing.

%package -n texlive-mpgraphics-doc
Summary:        Documentation for mpgraphics
Version:        svn29776.0.3

Provides:       tex-mpgraphics-doc
AutoReqProv:    No

%description -n texlive-mpgraphics-doc
Documentation for mpgraphics

%package -n texlive-musixguit
Provides:       tex-musixguit = %{tl_version}
License:        LPPL 1.3
Summary:        Easy notation for guitar music, in MusixTeX
Version:        svn21649.1.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(setspace.sty), tex(musixtex.sty), tex(musixper.tex), tex(musixgui.tex)
Provides:       tex(musixguit.sty) = %{tl_version}

%description -n texlive-musixguit
The package provides commands for typesetting notes for guitar,
especially for simplifying guitar notation with MusixTeX.

%package -n texlive-musixguit-doc
Summary:        Documentation for musixguit
Version:        svn21649.1.2.2

Provides:       tex-musixguit-doc
AutoReqProv:    No

%description -n texlive-musixguit-doc
Documentation for musixguit

%package -n texlive-musixtex-fonts
Provides:       tex-musixtex-fnts = %{tl_version}, tex-musixtex-fonts = %{tl_version}
Provides:       texlive-musixtex-fnts = %{tl_version}
Obsoletes:      texlive-musixtex-fnts < 2016
License:        GPL+
Summary:        Fonts used by MusixTeX
Version:        svn37762.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(musix.map) = %{tl_version}, tex(musix11.tfm) = %{tl_version}
Provides:       tex(musix13.tfm) = %{tl_version}, tex(musix16.tfm) = %{tl_version}
Provides:       tex(musix20.tfm) = %{tl_version}, tex(musix24.tfm) = %{tl_version}
Provides:       tex(musix25.tfm) = %{tl_version}, tex(musix29.tfm) = %{tl_version}
Provides:       tex(musixsps.tfm) = %{tl_version}, tex(musixspx.tfm) = %{tl_version}
Provides:       tex(mxsk.tfm) = %{tl_version}, tex(xadf11.tfm) = %{tl_version}
Provides:       tex(xadf13.tfm) = %{tl_version}, tex(xadf16.tfm) = %{tl_version}
Provides:       tex(xadf20.tfm) = %{tl_version}, tex(xadf24.tfm) = %{tl_version}
Provides:       tex(xadf29.tfm) = %{tl_version}, tex(xgreg11.tfm) = %{tl_version}
Provides:       tex(xgreg13.tfm) = %{tl_version}, tex(xgreg16.tfm) = %{tl_version}
Provides:       tex(xgreg20.tfm) = %{tl_version}, tex(xgreg24.tfm) = %{tl_version}
Provides:       tex(xgreg29.tfm) = %{tl_version}, tex(xppff10.tfm) = %{tl_version}
Provides:       tex(xsld11.tfm) = %{tl_version}, tex(xsld11d.tfm) = %{tl_version}
Provides:       tex(xsld13.tfm) = %{tl_version}, tex(xsld13d.tfm) = %{tl_version}
Provides:       tex(xsld16.tfm) = %{tl_version}, tex(xsld16d.tfm) = %{tl_version}
Provides:       tex(xsld20.tfm) = %{tl_version}, tex(xsld20d.tfm) = %{tl_version}
Provides:       tex(xsld24.tfm) = %{tl_version}, tex(xsld24d.tfm) = %{tl_version}
Provides:       tex(xsld29.tfm) = %{tl_version}, tex(xsld29d.tfm) = %{tl_version}
Provides:       tex(xsldd20.tfm) = %{tl_version}, tex(xsldu20.tfm) = %{tl_version}
Provides:       tex(xslhd11.tfm) = %{tl_version}, tex(xslhd11d.tfm) = %{tl_version}
Provides:       tex(xslhd13.tfm) = %{tl_version}, tex(xslhd13d.tfm) = %{tl_version}
Provides:       tex(xslhd16.tfm) = %{tl_version}, tex(xslhd16d.tfm) = %{tl_version}
Provides:       tex(xslhd20.tfm) = %{tl_version}, tex(xslhd20d.tfm) = %{tl_version}
Provides:       tex(xslhd24.tfm) = %{tl_version}, tex(xslhd24d.tfm) = %{tl_version}
Provides:       tex(xslhd29.tfm) = %{tl_version}, tex(xslhd29d.tfm) = %{tl_version}
Provides:       tex(xslhu11.tfm) = %{tl_version}, tex(xslhu11d.tfm) = %{tl_version}
Provides:       tex(xslhu13.tfm) = %{tl_version}, tex(xslhu13d.tfm) = %{tl_version}
Provides:       tex(xslhu16.tfm) = %{tl_version}, tex(xslhu16d.tfm) = %{tl_version}
Provides:       tex(xslhu20.tfm) = %{tl_version}, tex(xslhu20d.tfm) = %{tl_version}
Provides:       tex(xslhu20m.tfm) = %{tl_version}, tex(xslhu24.tfm) = %{tl_version}
Provides:       tex(xslhu24d.tfm) = %{tl_version}, tex(xslhu29.tfm) = %{tl_version}
Provides:       tex(xslhu29d.tfm) = %{tl_version}, tex(xslhz20.tfm) = %{tl_version}
Provides:       tex(xslhz20d.tfm) = %{tl_version}, tex(xslu11.tfm) = %{tl_version}
Provides:       tex(xslu11d.tfm) = %{tl_version}, tex(xslu13.tfm) = %{tl_version}
Provides:       tex(xslu13d.tfm) = %{tl_version}, tex(xslu16.tfm) = %{tl_version}
Provides:       tex(xslu16d.tfm) = %{tl_version}, tex(xslu20.tfm) = %{tl_version}
Provides:       tex(xslu20d.tfm) = %{tl_version}, tex(xslu24.tfm) = %{tl_version}
Provides:       tex(xslu24d.tfm) = %{tl_version}, tex(xslu29.tfm) = %{tl_version}
Provides:       tex(xslu29d.tfm) = %{tl_version}, tex(xslud20.tfm) = %{tl_version}
Provides:       tex(xslup20.tfm) = %{tl_version}, tex(xslz20.tfm) = %{tl_version}
Provides:       tex(xslz20d.tfm) = %{tl_version}, tex(xtie20.tfm) = %{tl_version}
Provides:       tex(musix11.pfb) = %{tl_version}, tex(musix13.pfb) = %{tl_version}
Provides:       tex(musix16.pfb) = %{tl_version}, tex(musix20.pfb) = %{tl_version}
Provides:       tex(musix24.pfb) = %{tl_version}, tex(musix29.pfb) = %{tl_version}
Provides:       tex(musixsps.pfb) = %{tl_version}, tex(musixspx.pfb) = %{tl_version}
Provides:       tex(mxsk.pfb) = %{tl_version}, tex(xadf11.pfb) = %{tl_version}
Provides:       tex(xadf13.pfb) = %{tl_version}, tex(xadf16.pfb) = %{tl_version}
Provides:       tex(xadf20.pfb) = %{tl_version}, tex(xadf24.pfb) = %{tl_version}
Provides:       tex(xadf29.pfb) = %{tl_version}, tex(xgreg11.pfb) = %{tl_version}
Provides:       tex(xgreg13.pfb) = %{tl_version}, tex(xgreg16.pfb) = %{tl_version}
Provides:       tex(xgreg20.pfb) = %{tl_version}, tex(xgreg24.pfb) = %{tl_version}
Provides:       tex(xgreg29.pfb) = %{tl_version}, tex(xppff10.pfb) = %{tl_version}
Provides:       tex(xsld11.pfb) = %{tl_version}, tex(xsld11d.pfb) = %{tl_version}
Provides:       tex(xsld13.pfb) = %{tl_version}, tex(xsld13d.pfb) = %{tl_version}
Provides:       tex(xsld16.pfb) = %{tl_version}, tex(xsld16d.pfb) = %{tl_version}
Provides:       tex(xsld20.pfb) = %{tl_version}, tex(xsld20d.pfb) = %{tl_version}
Provides:       tex(xsld24.pfb) = %{tl_version}, tex(xsld24d.pfb) = %{tl_version}
Provides:       tex(xsld29.pfb) = %{tl_version}, tex(xsld29d.pfb) = %{tl_version}
Provides:       tex(xsldd20.pfb) = %{tl_version}, tex(xsldu20.pfb) = %{tl_version}
Provides:       tex(xslhd11.pfb) = %{tl_version}, tex(xslhd11d.pfb) = %{tl_version}
Provides:       tex(xslhd13.pfb) = %{tl_version}, tex(xslhd13d.pfb) = %{tl_version}
Provides:       tex(xslhd16.pfb) = %{tl_version}, tex(xslhd16d.pfb) = %{tl_version}
Provides:       tex(xslhd20.pfb) = %{tl_version}, tex(xslhd20d.pfb) = %{tl_version}
Provides:       tex(xslhd24.pfb) = %{tl_version}, tex(xslhd24d.pfb) = %{tl_version}
Provides:       tex(xslhd29.pfb) = %{tl_version}, tex(xslhd29d.pfb) = %{tl_version}
Provides:       tex(xslhu11.pfb) = %{tl_version}, tex(xslhu11d.pfb) = %{tl_version}
Provides:       tex(xslhu13.pfb) = %{tl_version}, tex(xslhu13d.pfb) = %{tl_version}
Provides:       tex(xslhu16.pfb) = %{tl_version}, tex(xslhu16d.pfb) = %{tl_version}
Provides:       tex(xslhu20.pfb) = %{tl_version}, tex(xslhu20d.pfb) = %{tl_version}
Provides:       tex(xslhu24.pfb) = %{tl_version}, tex(xslhu24d.pfb) = %{tl_version}
Provides:       tex(xslhu29.pfb) = %{tl_version}, tex(xslhu29d.pfb) = %{tl_version}
Provides:       tex(xslhz20.pfb) = %{tl_version}, tex(xslhz20d.pfb) = %{tl_version}
Provides:       tex(xslu11.pfb) = %{tl_version}, tex(xslu11d.pfb) = %{tl_version}
Provides:       tex(xslu13.pfb) = %{tl_version}, tex(xslu13d.pfb) = %{tl_version}
Provides:       tex(xslu16.pfb) = %{tl_version}, tex(xslu16d.pfb) = %{tl_version}
Provides:       tex(xslu20.pfb) = %{tl_version}, tex(xslu20d.pfb) = %{tl_version}
Provides:       tex(xslu24.pfb) = %{tl_version}, tex(xslu24d.pfb) = %{tl_version}
Provides:       tex(xslu29.pfb) = %{tl_version}, tex(xslu29d.pfb) = %{tl_version}
Provides:       tex(xslud20.pfb) = %{tl_version}, tex(xslup20.pfb) = %{tl_version}
Provides:       tex(xslz20.pfb) = %{tl_version}, tex(xslz20d.pfb) = %{tl_version}
Provides:       tex(xtie20.pfb) = %{tl_version}, ctan-musixtex-fonts = %{tl_version}
Obsoletes:      ctan-musixtex-fonts < %{tl_version}

%description -n texlive-musixtex-fonts
These are fonts for use with MusixTeX; they are provided both
as original Metafont source, and as converted Adobe Type 1. The
bundle renders the older (Type 1 fonts only) bundle musixtex-
t1fonts obsolete.

%package -n texlive-musixtex-fonts-doc
Summary:        Documentation for musixtex-fnts
Provides:       tex-musixtex-fnts-doc = %{tl_version}, tex-musixtex-fonts-doc = %{tl_version}
Provides:       texlive-musixtex-fnts-doc = %{tl_version}
Obsoletes:      texlive-musixtex-fnts-doc < 2016
Version:        svn37762.0

AutoReqProv:    No

%description -n texlive-musixtex-fonts-doc
Documentation for musixtex-fnts

%package -n texlive-mxedruli
Provides:       tex-mxedruli = %{tl_version}
License:        LPPL
Summary:        A pair of fonts for different Georgian alphabets
Version:        svn30021.3.3c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(mxedruli.map) = %{tl_version}, tex(mxed10.tfm) = %{tl_version}
Provides:       tex(mxedbf10.tfm) = %{tl_version}, tex(mxedc10.tfm) = %{tl_version}
Provides:       tex(mxedi10.tfm) = %{tl_version}, tex(xuc10.tfm) = %{tl_version}
Provides:       tex(mxed10.pfb) = %{tl_version}, tex(mxedbf10.pfb) = %{tl_version}
Provides:       tex(mxedc10.pfb) = %{tl_version}, tex(mxedi10.pfb) = %{tl_version}
Provides:       tex(xuc10.pfb) = %{tl_version}, tex(mxedruli.sty) = %{tl_version}
Provides:       tex(umxed.fd) = %{tl_version}, tex(uxuc.fd) = %{tl_version}
Provides:       tex(xucuri.sty) = %{tl_version}

%description -n texlive-mxedruli
Two Georgian fonts, in both Metafont and Type 1 formats, which
cover the Mxedruli and the Xucuri alphabets.

%package -n texlive-mxedruli-doc
Summary:        Documentation for mxedruli
Version:        svn30021.3.3c

Provides:       tex-mxedruli-doc
AutoReqProv:    No

%description -n texlive-mxedruli-doc
Documentation for mxedruli

%package -n texlive-newsletr
Provides:       tex-newsletr = %{tl_version}
License:        Newsletr
Summary:        Macros for making newsletters with Plain TeX
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(newsletr.tex) = %{tl_version}

%description -n texlive-newsletr
newsletr package

%package -n texlive-newsletr-doc
Summary:        Documentation for newsletr
Version:        svn15878.0

Provides:       tex-newsletr-doc
AutoReqProv:    No

%description -n texlive-newsletr-doc
Documentation for newsletr

%package -n texlive-msu-thesis
Provides:       tex-msu-thesis = %{tl_version}
License:        LPPL 1.3
Summary:        Class for Michigan State University Master's and PhD theses
Version:        svn46106
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etex.sty), tex(pdflscape.sty), tex(tikz.sty)
Provides:       tex(gb4e-compat.tex) = %{tl_version}, tex(msu-thesis.cls) = %{tl_version}

%description -n texlive-msu-thesis
This is a class file for producing dissertations and theses
according to the Michigan State University Graduate School
Guidelines for Electronic Submission of Master's Theses and
Dissertations. The class should meet all current requirements
and is updated whenever the university guidelines change. The
class is based on the memoir document class, and inherits the
functionality of that class.

%package -n texlive-msu-thesis-doc
Summary:        Documentation for msu-thesis
Version:        svn46106
Provides:       tex-msu-thesis-doc
AutoReqProv:    No

%description -n texlive-msu-thesis-doc
Documentation for msu-thesis

%package -n texlive-mugsthesis
Provides:       tex-mugsthesis = %{tl_version}
License:        LPPL 1.3
Summary:        Thesis class complying with Marquette University Graduate School requirements
Version:        svn34878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(indentfirst.sty)
Provides:       tex(mugsthesis.cls) = %{tl_version}

%description -n texlive-mugsthesis
The bundle offers a thesis class, based on memoir, that
complies with Marquette University Graduate School
requirements.

%package -n texlive-mugsthesis-doc
Summary:        Documentation for mugsthesis
Version:        svn34878.0

Provides:       tex-mugsthesis-doc
AutoReqProv:    No

%description -n texlive-mugsthesis-doc
Documentation for mugsthesis

%package -n texlive-musuos
Provides:       tex-musuos = %{tl_version}
License:        LPPL
Summary:        Typeset papers for the department of music, Osnabruck
Version:        svn24857.1.1d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(environ.sty), tex(etoolbox.sty), tex(geometry.sty)
Requires:       tex(titletoc.sty), tex(csquotes.sty), tex(xspace.sty), tex(verse.sty)
Provides:       tex(musuos.cls) = %{tl_version}

%description -n texlive-musuos
The package provides a LaTeX class for typesetting term papers
at the institute of music and musicology of the University of
Osnabruck, Germany, according to the specifications of Prof.
Stefan Hahnheide. A biblatex style is provided.

%package -n texlive-musuos-doc
Summary:        Documentation for musuos
Version:        svn24857.1.1d

Provides:       tex-musuos-doc
AutoReqProv:    No

%description -n texlive-musuos-doc
Documentation for musuos

%package -n texlive-muthesis
Provides:       tex-muthesis = %{tl_version}
License:        LPPL
Summary:        Classes for University of Manchester Dept of Computer Science
Version:        svn23861.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(setspace.sty)
Provides:       tex(muthesis.cls) = %{tl_version}, tex(third-rep.cls) = %{tl_version}

%description -n texlive-muthesis
The bundle provides thesis and project report document classes
from the University of Manchester's Department of Computer
Science.

%package -n texlive-muthesis-doc
Summary:        Documentation for muthesis
Version:        svn23861.0

Provides:       tex-muthesis-doc
AutoReqProv:    No

%description -n texlive-muthesis-doc
Documentation for muthesis

%package -n texlive-nature
Provides:       tex-nature = %{tl_version}
License:        LPPL
Summary:        Prepare papers for the journal Nature
Version:        svn21819.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(cite.sty), tex(times.sty), tex(fullpage.sty), tex(ifthen.sty)
Provides:       tex(nature.cls) = %{tl_version}

%description -n texlive-nature
Nature does not accept papers in LaTeX, but it does accept PDF.
This class and BibTeX style provide what seems to be necessary
to produce papers in a format acceptable to the publisher.

%package -n texlive-nature-doc
Summary:        Documentation for nature
Version:        svn21819.1.0

Provides:       tex-nature-doc
AutoReqProv:    No

%description -n texlive-nature-doc
Documentation for nature

%package -n texlive-nddiss
Provides:       tex-nddiss = %{tl_version}
License:        LPPL
Summary:        Notre Dame Dissertation format class
Version:        svn45107
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(exscale.sty), tex(ifpdf.sty), tex(longtable.sty)
Requires:       tex(xspace.sty), tex(indentfirst.sty), tex(tabularx.sty), tex(enumerate.sty)
Requires:       tex(latexsym.sty), tex(showkeys.sty), tex(epsfig.sty), tex(color.sty)
Requires:       tex(graphicx.sty), tex(hyperref.sty), tex(natbib.sty), tex(hypernat.sty)
Requires:       tex(amsmath.sty), tex(amssymb.sty), tex(float.sty), tex(lscape.sty)
Requires:       tex(booktabs.sty), tex(rotating.sty), tex(url.sty), tex(setspace.sty)
Provides:       tex(nddiss2e.cls) = %{tl_version}

%description -n texlive-nddiss
This class file conforms to the requirements of the Graduate
School of the University of Notre Dame; with it a user can
format a thesis or dissertation in LaTeX.

%package -n texlive-nddiss-doc
Summary:        Documentation for nddiss
Version:        svn45107
Provides:       tex-nddiss-doc
AutoReqProv:    No

%description -n texlive-nddiss-doc
Documentation for nddiss

%package -n texlive-ndsu-thesis
Provides:       tex-ndsu-thesis = %{tl_version}
License:        LPPL 1.3
Summary:        North Dakota State University disquisition class
Version:        svn46639
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(ndsu-thesis.cls) = %{tl_version}

%description -n texlive-ndsu-thesis
A class for generating disquisitions, intended to be in
compliance with North Dakota State University requirements.

%package -n texlive-ndsu-thesis-doc
Summary:        Documentation for ndsu-thesis
Version:        svn46639
Provides:       tex-ndsu-thesis-doc
AutoReqProv:    No

%description -n texlive-ndsu-thesis-doc
Documentation for ndsu-thesis

%package -n texlive-nih
Provides:       tex-nih = %{tl_version}
License:        LPPL
Summary:        A class for NIH grant applications
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(helvet.sty), tex(geometry.sty), tex(fancyhdr.sty)
Requires:       tex(amsmath.sty)
Provides:       tex(denselists.sty) = %{tl_version}, tex(nih.cls) = %{tl_version}

%description -n texlive-nih
The nih class offers support for grant applications to NIH, the
National Institutes of Health, a US government agency. The
example-* files provide a template for using nih.cls and
submitting the biographical sketches the NIH wants. They
(potentially) use denselists package, which just reduces list
spacing; the package is distributed with the class, but is not
part of the class proper. (The examples may be distributed
without even the restrictions of the LaTeX licence.)

%package -n texlive-nih-doc
Summary:        Documentation for nih
Version:        svn15878.0

Provides:       tex-nih-doc
AutoReqProv:    No

%description -n texlive-nih-doc
Documentation for nih

%package -n texlive-mychemistry
Provides:       tex-mychemistry = %{tl_version}
License:        LPPL 1.3
Summary:        Create reaction schemes with LaTeX and ChemFig
Version:        svn28611.1.99b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(float.sty), tex(xkeyval.sty), tex(chemfig.sty)
Requires:       tex(chemmacros.sty), tex(translations.sty)
Provides:       tex(mychemistry.sty) = %{tl_version}

%description -n texlive-mychemistry
The package provides commands for typesetting complex chemical
reaction schemes with LaTeX and ChemFig. The package requires
the packages ChemFig, mhchem, chemcompounds and (sometimes)
chemexec.

%package -n texlive-mychemistry-doc
Summary:        Documentation for mychemistry
Version:        svn28611.1.99b

Provides:       tex-mychemistry-doc
AutoReqProv:    No

%description -n texlive-mychemistry-doc
Documentation for mychemistry

%package -n texlive-moodle-doc
Provides:       tex-moodle-doc = %{tl_version}
License:        LPPL
Summary:        doc files of moodle
Version:        svn39367

AutoReqProv:    No

%description -n texlive-moodle-doc
Documentation for moodle

%package -n texlive-moodle
Provides:       tex-moodle = %{tl_version}
License:        LPPL
Summary:        Generating Moodle quizzes via LaTeX
Version:        svn39367

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(moodle.sty) = %{tl_version}

%description -n texlive-moodle
A package for writing Moodle quizzes in LaTeX. In addition to
typesetting the quizzes for proofreading, the package compiles
an XML file to be uploaded to a Moodle server.

%package -n texlive-mparrows-doc
Provides:       tex-mparrows-doc = %{tl_version}
License:        GPLv3+
Summary:        doc files of mparrows
Version:        svn39729

AutoReqProv:    No

%description -n texlive-mparrows-doc
Documentation for mparrows

%package -n texlive-mparrows
Provides:       tex-mparrows = %{tl_version}
License:        Public Domain
Summary:        MetaPost module with different types of arrow heads
Version:        svn39729

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-mparrows
A package to provide different types of arrow heads to be used
with MetaPost commands drawarrow and drawdblarrow commands.

%package -n texlive-multidef-doc
Provides:       tex-multidef-doc = %{tl_version}
License:        LPPL
Summary:        doc files of multidef
Version:        svn40637

AutoReqProv:    No

%description -n texlive-multidef-doc
Documentation for multidef

%package -n texlive-multidef
Provides:       tex-multidef = %{tl_version}
License:        LPPL
Summary:        Quickly define several similar macros
Version:        svn40637

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(multidef.sty) = %{tl_version}

%description -n texlive-multidef
Multidef provides a simple way of defining several macros
having similar definitions.

%package -n texlive-mynsfc-doc
Provides:       tex-mynsfc-doc = %{tl_version}
License:        LPPL
Summary:        doc files of mynsfc
Version:        svn41996
AutoReqProv:    No

%description -n texlive-mynsfc-doc
Documentation for mynsfc

%package -n texlive-mynsfc
Provides:       tex-mynsfc = %{tl_version}
License:        LPPL
Summary:        XeLaTeX template for writing the main body of NSFC proposals
Version:        svn41996
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(mynsfc.cls) = %{tl_version}

%description -n texlive-mynsfc
The package provides a XeLaTeX template for writing the main
body of National Natural Science Foundation of China (NSFC)
proposals, which are allowed to apply online. The package
defines styles of the outlines and uses BibLaTeX/biber for the
management of references.

%package -n texlive-nihbiosketch-doc
Provides:       tex-nihbiosketch-doc = %{tl_version}
License:        LPPL
Summary:        doc files of nihbiosketch
Version:        svn39460

AutoReqProv:    No

%description -n texlive-nihbiosketch-doc
Documentation for nihbiosketch

%package -n texlive-nihbiosketch
Provides:       tex-nihbiosketch = %{tl_version}
License:        LPPL
Summary:        A class for NIH biosketches based on the 2015 updated format
Version:        svn39460

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(nihbiosketch.cls) = %{tl_version}

%description -n texlive-nihbiosketch
This LaTeX document class tries to adhere to the Biographical
Sketch formatting requirements outlined in NIH Notice [NOT-OD-
15-032] (http://grants.nih.gov/grants/guide/notice-files/NOT-OD-
15-032.html). This new format is required for applications
submitted for due dates on or after May 25, 2015. The package
tries to mimic the example documents provided on the [SF 424
(R&R) Forms and Applications page]
(http://grants.nih.gov/grants/funding/424/index.htm#format) as
closely as possible. The author has used this class for his own
grant submissions; however he offers no guarantee of conformity
to NIH requirements.

%package -n texlive-nimbus15-doc
Provides:       tex-nimbus15-doc = %{tl_version}
License:        AGPLv3 with exceptions and LPPL
Summary:        doc files of nimbus15
Version:        svn39343

AutoReqProv:    No

%description -n texlive-nimbus15-doc
Documentation for nimbus15

%package -n texlive-nimbus15
Provides:       tex-nimbus15 = %{tl_version}
License:        AGPLv3 with exceptions and LPPL
Summary:        Support files for Nimbus 2015 Core fonts
Version:        svn39343

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(nimbussans.sty) = %{tl_version}, tex(nimbusmono.sty) = %{tl_version}
Provides:       tex(nimbusmononarrow.sty) = %{tl_version}
Provides:       tex(nimbusserif.sty) = %{tl_version}, tex(nimbus15.map) = %{tl_version}
Provides:       tex(T2BNimbusMono.fd) = %{tl_version}, tex(T2ANimbusMono.fd) = %{tl_version}
Provides:       tex(TS1NimbusMono.fd) = %{tl_version}, tex(LGRNimbusSerif.fd) = %{tl_version}
Provides:       tex(T2CNimbusMonoN.fd) = %{tl_version}, tex(OT2NimbusMonoN.fd) = %{tl_version}
Provides:       tex(T1NimbusSans.fd) = %{tl_version}, tex(T2ANimbusSans.fd) = %{tl_version}
Provides:       tex(T1NimbusMono.fd) = %{tl_version}, tex(OT2NimbusSans.fd) = %{tl_version}
Provides:       tex(T2CNimbusSerif.fd) = %{tl_version}, tex(T2BNimbusSans.fd) = %{tl_version}
Provides:       tex(OT1NimbusSans.fd) = %{tl_version}, tex(LGRNimbuSans.fd) = %{tl_version}
Provides:       tex(OT1NimbusSerif.fd) = %{tl_version}, tex(T2ANimbusSerif.fd) = %{tl_version}
Provides:       tex(TS1NimbusMonoN.fd) = %{tl_version}, tex(T2CNimbusSans.fd) = %{tl_version}
Provides:       tex(OT2NimbusSerif.fd) = %{tl_version}, tex(TS1NimbusSans.fd) = %{tl_version}
Provides:       tex(T1NimbusSerif.fd) = %{tl_version}, tex(T2BNimbusMonoN.fd) = %{tl_version}
Provides:       tex(TS1NimbusSerif.fd) = %{tl_version}, tex(LGRNimbusMonoN.fd) = %{tl_version}
Provides:       tex(OT1NimbusMono.fd) = %{tl_version}, tex(T2BNimbusSerif.fd) = %{tl_version}
Provides:       tex(T2CNimbusMono.fd) = %{tl_version}, tex(T1NimbusMonoN.fd) = %{tl_version}
Provides:       tex(OT1NimbusMonoN.fd) = %{tl_version}, tex(LGRNimbusMono.fd) = %{tl_version}
Provides:       tex(T2ANimbusMonoN.fd) = %{tl_version}, tex(OT2NimbusMono.fd) = %{tl_version}
Provides:       tex(zcoN-Oblique.pfb) = %{tl_version}, tex(zco-Oblique.pfb) = %{tl_version}
Provides:       tex(ztm-Reg.pfb) = %{tl_version}, tex(zco-LightOblique.pfb) = %{tl_version}
Provides:       tex(zhv-Bol.pfb) = %{tl_version}, tex(zco-BoldOblique.pfb) = %{tl_version}
Provides:       tex(zco-Regular.pfb) = %{tl_version}, tex(ztm-RegObl.pfb) = %{tl_version}
Provides:       tex(zco-Bold.pfb) = %{tl_version}, tex(zhv-BolIta.pfb) = %{tl_version}
Provides:       tex(zhv-Reg.pfb) = %{tl_version}, tex(ztm-RegIta.pfb) = %{tl_version}
Provides:       tex(zco-Light.pfb) = %{tl_version}, tex(zhv-RegIta.pfb) = %{tl_version}
Provides:       tex(zcoN-Regular.pfb) = %{tl_version}, tex(ztm-MedObl.pfb) = %{tl_version}
Provides:       tex(ztm-Med.pfb) = %{tl_version}, tex(ztm-MedIta.pfb) = %{tl_version}
Provides:       tex(nimbus15mono-t2a.enc) = %{tl_version}
Provides:       tex(nimbus15-t2c.enc) = %{tl_version}, tex(nimbus15mono-ot2.enc) = %{tl_version}
Provides:       tex(nimbus15-t2a.enc) = %{tl_version}, tex(nimbus15-ot1.enc) = %{tl_version}
Provides:       tex(nimbus15mono-lgr.enc) = %{tl_version}
Provides:       tex(nimbus15mono-t2c.enc) = %{tl_version}
Provides:       tex(nimbus15mono-ec.enc) = %{tl_version}
Provides:       tex(nimbus15-ot2.enc) = %{tl_version}, tex(nimbus15-ec.enc) = %{tl_version}
Provides:       tex(nimbus15-lgr.enc) = %{tl_version}, tex(nimbus15-t2b.enc) = %{tl_version}
Provides:       tex(nimbus15mono-ot1.enc) = %{tl_version}
Provides:       tex(nimbus15mono-t2b.enc) = %{tl_version}
Provides:       tex(nimbus15-x2.enc) = %{tl_version}, tex(zcoN-Oblique.otf) = %{tl_version}
Provides:       tex(zco-Bold.otf) = %{tl_version}, tex(ztm-MedIta.otf) = %{tl_version}
Provides:       tex(ztm-RegIta.otf) = %{tl_version}, tex(zhv-RegIta.otf) = %{tl_version}
Provides:       tex(zco-BoldOblique.otf) = %{tl_version}
Provides:       tex(ztm-Reg.otf) = %{tl_version}, tex(ztm-MedObl.otf) = %{tl_version}
Provides:       tex(zco-Oblique.otf) = %{tl_version}, tex(ztm-Med.otf) = %{tl_version}
Provides:       tex(ztm-RegObl.otf) = %{tl_version}, tex(zco-Light.otf) = %{tl_version}
Provides:       tex(zhv-BolIta.otf) = %{tl_version}, tex(zcoN-Regular.otf) = %{tl_version}
Provides:       tex(zhv-Reg.otf) = %{tl_version}, tex(zco-LightOblique.otf) = %{tl_version}
Provides:       tex(zhv-Bol.otf) = %{tl_version}, tex(zco-Regular.otf) = %{tl_version}
Provides:       tex(ztm-RegIta-ot2.vf) = %{tl_version}, tex(ztm-RegObl-ot2.vf) = %{tl_version}
Provides:       tex(zhv-BolIta-ot2.vf) = %{tl_version}, tex(ztm-MedObl-ot2.vf) = %{tl_version}
Provides:       tex(zco-Oblique-ot2.vf) = %{tl_version}, tex(zhv-RegIta-ot2.vf) = %{tl_version}
Provides:       tex(zhv-Reg-ot2.vf) = %{tl_version}, tex(zcoN-Regular-ot2.vf) = %{tl_version}
Provides:       tex(zco-Regular-ot2.vf) = %{tl_version}, tex(zhv-Bol-ot2.vf) = %{tl_version}
Provides:       tex(ztm-Med-ot2.vf) = %{tl_version}, tex(ztm-MedIta-ot2.vf) = %{tl_version}
Provides:       tex(ztm-Reg-ot2.vf) = %{tl_version}, tex(zco-Bold-ot2.vf) = %{tl_version}
Provides:       tex(zco-Light-ot2.vf) = %{tl_version}, tex(zcoN-Oblique-ot2.vf) = %{tl_version}
Provides:       tex(zco-LightOblique-ot2.vf) = %{tl_version}
Provides:       tex(zco-BoldOblique-ot2.vf) = %{tl_version}
Provides:       tex(zhv-Bol-t2c.tfm) = %{tl_version}, tex(zco-LightOblique-ot1.tfm) = %{tl_version}
Provides:       tex(zhv-BolIta-t1.tfm) = %{tl_version}, tex(zcoN-Oblique-ot2--base.tfm) = %{tl_version}
Provides:       tex(ztm-RegIta-ot2--base.tfm) = %{tl_version}
Provides:       tex(zcoN-Regular-t2a.tfm) = %{tl_version}
Provides:       tex(zhv-Bol-ts1.tfm) = %{tl_version}, tex(zhv-RegIta-lgr.tfm) = %{tl_version}
Provides:       tex(zco-BoldOblique-ts1.tfm) = %{tl_version}
Provides:       tex(zco-BoldOblique-lgr.tfm) = %{tl_version}
Provides:       tex(zco-Light-ot1.tfm) = %{tl_version}, tex(ztm-RegObl-ot2--base.tfm) = %{tl_version}
Provides:       tex(zhv-Bol-t2b.tfm) = %{tl_version}, tex(zco-LightOblique-t2a.tfm) = %{tl_version}
Provides:       tex(zcoN-Regular-t2b.tfm) = %{tl_version}
Provides:       tex(zcoN-Oblique-ts1.tfm) = %{tl_version}
Provides:       tex(zhv-RegIta-t2b.tfm) = %{tl_version}, tex(zco-Regular-lgr.tfm) = %{tl_version}
Provides:       tex(zhv-BolIta-ot2--base.tfm) = %{tl_version}
Provides:       tex(ztm-Med-ot2--base.tfm) = %{tl_version}
Provides:       tex(zco-Bold-t2b.tfm) = %{tl_version}, tex(zco-Bold-t1.tfm) = %{tl_version}
Provides:       tex(zco-BoldOblique-ot2.tfm) = %{tl_version}
Provides:       tex(ztm-RegIta-ot2.tfm) = %{tl_version}, tex(ztm-RegObl-t2c.tfm) = %{tl_version}
Provides:       tex(zcoN-Oblique-t2a.tfm) = %{tl_version}
Provides:       tex(ztm-RegIta-lgr.tfm) = %{tl_version}, tex(ztm-Med-ot1.tfm) = %{tl_version}
Provides:       tex(zco-BoldOblique-t1.tfm) = %{tl_version}
Provides:       tex(zco-Regular-ot2--base.tfm) = %{tl_version}
Provides:       tex(zco-BoldOblique-t2b.tfm) = %{tl_version}
Provides:       tex(ztm-Reg-ot1.tfm) = %{tl_version}, tex(zco-Light-t2a.tfm) = %{tl_version}
Provides:       tex(zhv-RegIta-t1.tfm) = %{tl_version}, tex(ztm-Med-t2a.tfm) = %{tl_version}
Provides:       tex(zhv-Reg-ot2.tfm) = %{tl_version}, tex(zcoN-Regular-lgr.tfm) = %{tl_version}
Provides:       tex(zco-Light-t2c.tfm) = %{tl_version}, tex(zcoN-Oblique-ot1.tfm) = %{tl_version}
Provides:       tex(zco-Oblique-lgr.tfm) = %{tl_version}
Provides:       tex(zhv-Reg-t2a.tfm) = %{tl_version}, tex(zco-BoldOblique-t2a.tfm) = %{tl_version}
Provides:       tex(zcoN-Oblique-t1.tfm) = %{tl_version}
Provides:       tex(zhv-Bol-ot1.tfm) = %{tl_version}, tex(zco-Light.tfm) = %{tl_version}
Provides:       tex(zco-LightOblique-lgr.tfm) = %{tl_version}
Provides:       tex(ztm-MedObl-ot1.tfm) = %{tl_version}, tex(zhv-BolIta-ot1.tfm) = %{tl_version}
Provides:       tex(ztm-MedIta-t2c.tfm) = %{tl_version}, tex(ztm-MedIta-lgr.tfm) = %{tl_version}
Provides:       tex(zhv-BolIta-t2c.tfm) = %{tl_version}, tex(zhv-BolIta-t2b.tfm) = %{tl_version}
Provides:       tex(ztm-Reg-t2c.tfm) = %{tl_version}, tex(ztm-Med-t2c.tfm) = %{tl_version}
Provides:       tex(zco-Regular-t2b.tfm) = %{tl_version}
Provides:       tex(ztm-MedIta-t1.tfm) = %{tl_version}, tex(zco-Bold-t2a.tfm) = %{tl_version}
Provides:       tex(zcoN-Regular-t1.tfm) = %{tl_version}
Provides:       tex(ztm-Med-t1.tfm) = %{tl_version}, tex(zhv-Reg-ts1.tfm) = %{tl_version}
Provides:       tex(ztm-MedIta-ot1.tfm) = %{tl_version}, tex(ztm-Med-t2b.tfm) = %{tl_version}
Provides:       tex(zhv-RegIta-ts1.tfm) = %{tl_version}, tex(zhv-Bol-t1.tfm) = %{tl_version}
Provides:       tex(ztm-Reg-ot2--base.tfm) = %{tl_version}
Provides:       tex(ztm-Med-ot2.tfm) = %{tl_version}, tex(ztm-Reg-lgr.tfm) = %{tl_version}
Provides:       tex(zhv-RegIta-t2c.tfm) = %{tl_version}, tex(zcoN-Oblique-t2c.tfm) = %{tl_version}
Provides:       tex(ztm-RegObl-t1.tfm) = %{tl_version}, tex(zhv-BolIta-t2a.tfm) = %{tl_version}
Provides:       tex(zcoN-Regular-ot2--base.tfm) = %{tl_version}
Provides:       tex(ztm-Reg-t2b.tfm) = %{tl_version}, tex(ztm-Reg-ts1.tfm) = %{tl_version}
Provides:       tex(zco-Light-ot2--base.tfm) = %{tl_version}
Provides:       tex(ztm-MedObl-ot2.tfm) = %{tl_version}, tex(zco-Light-t2b.tfm) = %{tl_version}
Provides:       tex(zco-Oblique-ot2--base.tfm) = %{tl_version}
Provides:       tex(ztm-Med-ts1.tfm) = %{tl_version}, tex(ztm-RegIta-t1.tfm) = %{tl_version}
Provides:       tex(zhv-Reg-t2b.tfm) = %{tl_version}, tex(zhv-Reg-lgr.tfm) = %{tl_version}
Provides:       tex(zco-Regular-ot2.tfm) = %{tl_version}
Provides:       tex(ztm-MedObl-t1.tfm) = %{tl_version}, tex(ztm-RegObl-t2b.tfm) = %{tl_version}
Provides:       tex(zhv-Reg-t2c.tfm) = %{tl_version}, tex(zco-Light-lgr.tfm) = %{tl_version}
Provides:       tex(ztm-RegIta-ts1.tfm) = %{tl_version}, tex(zco-Regular-ot1.tfm) = %{tl_version}
Provides:       tex(ztm-RegObl-lgr.tfm) = %{tl_version}, tex(zhv-RegIta-ot1.tfm) = %{tl_version}
Provides:       tex(zhv-RegIta-ot2--base.tfm) = %{tl_version}
Provides:       tex(ztm-MedObl-t2c.tfm) = %{tl_version}, tex(zcoN-Oblique-lgr.tfm) = %{tl_version}
Provides:       tex(zco-LightOblique-t2c.tfm) = %{tl_version}
Provides:       tex(zco-Bold-ot1.tfm) = %{tl_version}, tex(zcoN-Regular-t2c.tfm) = %{tl_version}
Provides:       tex(zco-BoldOblique-t2c.tfm) = %{tl_version}
Provides:       tex(zco-Oblique-ot1.tfm) = %{tl_version}
Provides:       tex(zco-Regular-ts1.tfm) = %{tl_version}
Provides:       tex(ztm-MedObl-ot2--base.tfm) = %{tl_version}
Provides:       tex(zhv-BolIta-ot2.tfm) = %{tl_version}, tex(ztm-MedIta-ts1.tfm) = %{tl_version}
Provides:       tex(ztm-RegIta-t2b.tfm) = %{tl_version}, tex(zco-Light-ot2.tfm) = %{tl_version}
Provides:       tex(ztm-RegObl-t2a.tfm) = %{tl_version}, tex(ztm-RegIta-ot1.tfm) = %{tl_version}
Provides:       tex(ztm-MedObl-lgr.tfm) = %{tl_version}, tex(ztm-RegObl-ot2.tfm) = %{tl_version}
Provides:       tex(zhv-BolIta-lgr.tfm) = %{tl_version}, tex(zco-Regular-t1.tfm) = %{tl_version}
Provides:       tex(zco-Oblique-t2b.tfm) = %{tl_version}
Provides:       tex(zco-Oblique-ts1.tfm) = %{tl_version}
Provides:       tex(zco-Oblique-t1.tfm) = %{tl_version}, tex(zco-Oblique-t2c.tfm) = %{tl_version}
Provides:       tex(zhv-Bol-t2a.tfm) = %{tl_version}, tex(ztm-MedObl-t2b.tfm) = %{tl_version}
Provides:       tex(zhv-Reg-ot1.tfm) = %{tl_version}, tex(ztm-MedObl-ts1.tfm) = %{tl_version}
Provides:       tex(zhv-RegIta-t2a.tfm) = %{tl_version}, tex(ztm-RegIta-t2a.tfm) = %{tl_version}
Provides:       tex(zco-LightOblique-t2b.tfm) = %{tl_version}
Provides:       tex(zco-Light-t1.tfm) = %{tl_version}, tex(zhv-Bol-ot2.tfm) = %{tl_version}
Provides:       tex(zhv-Reg-t1.tfm) = %{tl_version}, tex(zcoN-Regular-ts1.tfm) = %{tl_version}
Provides:       tex(ztm-RegIta-t2c.tfm) = %{tl_version}, tex(ztm-RegObl-ts1.tfm) = %{tl_version}
Provides:       tex(zco-Oblique-ot2.tfm) = %{tl_version}
Provides:       tex(zco-Regular-t2a.tfm) = %{tl_version}
Provides:       tex(zco-Regular-t2c.tfm) = %{tl_version}
Provides:       tex(ztm-RegObl-ot1.tfm) = %{tl_version}, tex(ztm-MedObl-t2a.tfm) = %{tl_version}
Provides:       tex(zcoN-Regular-ot2.tfm) = %{tl_version}
Provides:       tex(zcoN-Regular-ot1.tfm) = %{tl_version}
Provides:       tex(zcoN-Oblique-t2b.tfm) = %{tl_version}
Provides:       tex(zco-LightOblique-t1.tfm) = %{tl_version}
Provides:       tex(zhv-Bol-ot2--base.tfm) = %{tl_version}
Provides:       tex(zco-Bold-t2c.tfm) = %{tl_version}, tex(zco-Bold-ot2--base.tfm) = %{tl_version}
Provides:       tex(zcoN-Oblique-ot2.tfm) = %{tl_version}
Provides:       tex(zco-Bold-ts1.tfm) = %{tl_version}, tex(zco-Oblique-t2a.tfm) = %{tl_version}
Provides:       tex(zco-LightOblique-ot2--base.tfm) = %{tl_version}
Provides:       tex(zco-LightOblique-ot2.tfm) = %{tl_version}
Provides:       tex(zhv-BolIta-ts1.tfm) = %{tl_version}, tex(zco-LightOblique-ts1.tfm) = %{tl_version}
Provides:       tex(zco-BoldOblique-ot2--base.tfm) = %{tl_version}
Provides:       tex(zco-Light-ts1.tfm) = %{tl_version}, tex(zco-BoldOblique-ot1.tfm) = %{tl_version}
Provides:       tex(ztm-Reg-t2a.tfm) = %{tl_version}, tex(ztm-Reg-t1.tfm) = %{tl_version}
Provides:       tex(ztm-MedIta-t2a.tfm) = %{tl_version}, tex(zhv-Bol-lgr.tfm) = %{tl_version}
Provides:       tex(zhv-Reg-ot2--base.tfm) = %{tl_version}
Provides:       tex(ztm-Reg-ot2.tfm) = %{tl_version}, tex(ztm-Med-lgr.tfm) = %{tl_version}
Provides:       tex(zco-Bold-lgr.tfm) = %{tl_version}, tex(ztm-MedIta-ot2.tfm) = %{tl_version}
Provides:       tex(ztm-MedIta-t2b.tfm) = %{tl_version}, tex(zhv-RegIta-ot2.tfm) = %{tl_version}
Provides:       tex(ztm-MedIta-ot2--base.tfm) = %{tl_version}
Provides:       tex(zco-Bold-ot2.tfm) = %{tl_version}

%description -n texlive-nimbus15
The Nimbus 2015 Core fonts added Greek and Cyrillic glyphs.
This package may be best suited as an add-on the a
comprehensive Times package, providing support for Greek and
Cyrillic. A new intermediate weight of NimbusMono (AKA Courier)
is provided, along with a narrower version which may be useful
for rendering code.

%package -n texlive-modular
Summary:        Relative section headings for modular documents
Version:        svn44142
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(modular.sty) = %{tl_version}

%description -n texlive-modular
LaTeX sections have absolute depth, e.g. \section, \subsection,
etc. When composing modular documents, we want relative depths.
The coseoul package provides relative headings, but does not
get things right when composing a document modularly from
multiple parts. This package provides the missing piece.
modular relies on coseoul, import, and ifthen.

%package -n texlive-montserrat
Summary:        Montserrat sans serif, otf and pfb, with LaTeX support files
Version:        svn43347
License:        OFL and LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(zmo_2475kw.enc) = %{tl_version}, tex(zmo_2wpmsr.enc) = %{tl_version}
Provides:       tex(zmo_35dncn.enc) = %{tl_version}, tex(zmo_3757re.enc) = %{tl_version}
Provides:       tex(zmo_3afaux.enc) = %{tl_version}, tex(zmo_3xgpuk.enc) = %{tl_version}
Provides:       tex(zmo_3xjnji.enc) = %{tl_version}, tex(zmo_46rasm.enc) = %{tl_version}
Provides:       tex(zmo_4jynbq.enc) = %{tl_version}, tex(zmo_4teuyg.enc) = %{tl_version}
Provides:       tex(zmo_4upncp.enc) = %{tl_version}, tex(zmo_544jjb.enc) = %{tl_version}
Provides:       tex(zmo_56el2v.enc) = %{tl_version}, tex(zmo_5fadnl.enc) = %{tl_version}
Provides:       tex(zmo_5rna26.enc) = %{tl_version}, tex(zmo_5ubf37.enc) = %{tl_version}
Provides:       tex(zmo_5z3jz7.enc) = %{tl_version}, tex(zmo_67twef.enc) = %{tl_version}
Provides:       tex(zmo_bd3o7d.enc) = %{tl_version}, tex(zmo_bdtbcv.enc) = %{tl_version}
Provides:       tex(zmo_bkgosm.enc) = %{tl_version}, tex(zmo_byz2kr.enc) = %{tl_version}
Provides:       tex(zmo_c5wpta.enc) = %{tl_version}, tex(zmo_cegcqk.enc) = %{tl_version}
Provides:       tex(zmo_d2kyeu.enc) = %{tl_version}, tex(zmo_daczqg.enc) = %{tl_version}
Provides:       tex(zmo_dr7oop.enc) = %{tl_version}, tex(zmo_eh44de.enc) = %{tl_version}
Provides:       tex(zmo_es6tpc.enc) = %{tl_version}, tex(zmo_f642ba.enc) = %{tl_version}
Provides:       tex(zmo_fxccce.enc) = %{tl_version}, tex(zmo_gttaze.enc) = %{tl_version}
Provides:       tex(zmo_hau3x5.enc) = %{tl_version}, tex(zmo_hybuin.enc) = %{tl_version}
Provides:       tex(zmo_i2wmyu.enc) = %{tl_version}, tex(zmo_iabfdf.enc) = %{tl_version}
Provides:       tex(zmo_ijcy2e.enc) = %{tl_version}, tex(zmo_ivvhub.enc) = %{tl_version}
Provides:       tex(zmo_jumqgp.enc) = %{tl_version}, tex(zmo_k3ucka.enc) = %{tl_version}
Provides:       tex(zmo_kg3mv7.enc) = %{tl_version}, tex(zmo_kpjbgw.enc) = %{tl_version}
Provides:       tex(zmo_ktszbv.enc) = %{tl_version}, tex(zmo_l6ekdc.enc) = %{tl_version}
Provides:       tex(zmo_ljoz2a.enc) = %{tl_version}, tex(zmo_loozhj.enc) = %{tl_version}
Provides:       tex(zmo_m7viqr.enc) = %{tl_version}, tex(zmo_mpjdp6.enc) = %{tl_version}
Provides:       tex(zmo_myxsx6.enc) = %{tl_version}, tex(zmo_n233ks.enc) = %{tl_version}
Provides:       tex(zmo_n73q35.enc) = %{tl_version}, tex(zmo_nimoma.enc) = %{tl_version}
Provides:       tex(zmo_nyafwi.enc) = %{tl_version}, tex(zmo_o4eebi.enc) = %{tl_version}
Provides:       tex(zmo_o4tig7.enc) = %{tl_version}, tex(zmo_o7oh2z.enc) = %{tl_version}
Provides:       tex(zmo_ogifq5.enc) = %{tl_version}, tex(zmo_olufhi.enc) = %{tl_version}
Provides:       tex(zmo_ov66hc.enc) = %{tl_version}, tex(zmo_pgha5c.enc) = %{tl_version}
Provides:       tex(zmo_pk4ncj.enc) = %{tl_version}, tex(zmo_pogoar.enc) = %{tl_version}
Provides:       tex(zmo_ps2jnw.enc) = %{tl_version}, tex(zmo_pslnjt.enc) = %{tl_version}
Provides:       tex(zmo_pub5az.enc) = %{tl_version}, tex(zmo_qp4jag.enc) = %{tl_version}
Provides:       tex(zmo_qqaxlq.enc) = %{tl_version}, tex(zmo_rfo7vr.enc) = %{tl_version}
Provides:       tex(zmo_s7irvx.enc) = %{tl_version}, tex(zmo_scppf7.enc) = %{tl_version}
Provides:       tex(zmo_skw6h2.enc) = %{tl_version}, tex(zmo_slhote.enc) = %{tl_version}
Provides:       tex(zmo_subnof.enc) = %{tl_version}, tex(zmo_tjcog7.enc) = %{tl_version}
Provides:       tex(zmo_tjhwyu.enc) = %{tl_version}, tex(zmo_tni2lj.enc) = %{tl_version}
Provides:       tex(zmo_ts2hdt.enc) = %{tl_version}, tex(zmo_txtt2v.enc) = %{tl_version}
Provides:       tex(zmo_uqa4kb.enc) = %{tl_version}, tex(zmo_utxkra.enc) = %{tl_version}
Provides:       tex(zmo_v3m2pu.enc) = %{tl_version}, tex(zmo_vmhiwp.enc) = %{tl_version}
Provides:       tex(zmo_vrs6kn.enc) = %{tl_version}, tex(zmo_w43b7b.enc) = %{tl_version}
Provides:       tex(zmo_wieltn.enc) = %{tl_version}, tex(zmo_wuqpdh.enc) = %{tl_version}
Provides:       tex(zmo_wvuz2i.enc) = %{tl_version}, tex(zmo_wygu6d.enc) = %{tl_version}
Provides:       tex(zmo_x7rqlm.enc) = %{tl_version}, tex(zmo_xey7lb.enc) = %{tl_version}
Provides:       tex(zmo_xu2liq.enc) = %{tl_version}, tex(zmo_xu4w3w.enc) = %{tl_version}
Provides:       tex(zmo_yntdxo.enc) = %{tl_version}, tex(zmo_ytfxzt.enc) = %{tl_version}
Provides:       tex(zmo_yyqg6d.enc) = %{tl_version}, tex(zmo_z64ahx.enc) = %{tl_version}
Provides:       tex(zmo_zfphbh.enc) = %{tl_version}, tex(montserrat.map) = %{tl_version}
Provides:       tex(Montserrat-Black.otf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic.otf) = %{tl_version}
Provides:       tex(Montserrat-Bold.otf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic.otf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold.otf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic.otf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight.otf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic.otf) = %{tl_version}
Provides:       tex(Montserrat-Italic.otf) = %{tl_version}
Provides:       tex(Montserrat-Light.otf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic.otf) = %{tl_version}
Provides:       tex(Montserrat-Medium.otf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic.otf) = %{tl_version}
Provides:       tex(Montserrat-Regular.otf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold.otf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic.otf) = %{tl_version}
Provides:       tex(Montserrat-Thin.otf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin.otf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic.otf) = %{tl_version}
Provides:       tex(Montserrat-Black-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Montserrat-Black.pfb) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic.pfb) = %{tl_version}
Provides:       tex(Montserrat-Bold.pfb) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold.pfb) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic.pfb) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight.pfb) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic.pfb) = %{tl_version}
Provides:       tex(Montserrat-Italic.pfb) = %{tl_version}
Provides:       tex(Montserrat-Light.pfb) = %{tl_version}
Provides:       tex(Montserrat-LightItalic.pfb) = %{tl_version}
Provides:       tex(Montserrat-Medium.pfb) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic.pfb) = %{tl_version}
Provides:       tex(Montserrat-Regular.pfb) = %{tl_version}
Provides:       tex(Montserrat-SemiBold.pfb) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic.pfb) = %{tl_version}
Provides:       tex(Montserrat-Thin.pfb) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-Black.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-Light.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin.pfb) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic.pfb) = %{tl_version}
Provides:       tex(montserrat.sty) = %{tl_version}, tex(Montserrat-Black-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Black-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BlackItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraBoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLight-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ExtraLightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-LightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Medium-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-MediumItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-SemiBoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-Thin-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Montserrat-ThinItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Black-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BlackItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraBoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLight-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ExtraLightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-LightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Medium-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-MediumItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-SemiBoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-Thin-tosf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(MontserratAlternates-ThinItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Montserrat-Dnom.fd) = %{tl_version}
Provides:       tex(LY1Montserrat-Inf.fd) = %{tl_version}
Provides:       tex(LY1Montserrat-LF.fd) = %{tl_version}
Provides:       tex(LY1Montserrat-Numr.fd) = %{tl_version}
Provides:       tex(LY1Montserrat-OsF.fd) = %{tl_version}
Provides:       tex(LY1Montserrat-Sup.fd) = %{tl_version}
Provides:       tex(LY1Montserrat-TLF.fd) = %{tl_version}
Provides:       tex(LY1Montserrat-TOsF.fd) = %{tl_version}
Provides:       tex(LY1MontserratAlternates-Dnom.fd) = %{tl_version}
Provides:       tex(LY1MontserratAlternates-Inf.fd) = %{tl_version}
Provides:       tex(LY1MontserratAlternates-LF.fd) = %{tl_version}
Provides:       tex(LY1MontserratAlternates-Numr.fd) = %{tl_version}
Provides:       tex(LY1MontserratAlternates-OsF.fd) = %{tl_version}
Provides:       tex(LY1MontserratAlternates-Sup.fd) = %{tl_version}
Provides:       tex(LY1MontserratAlternates-TLF.fd) = %{tl_version}
Provides:       tex(LY1MontserratAlternates-TOsF.fd) = %{tl_version}
Provides:       tex(OT1Montserrat-Dnom.fd) = %{tl_version}
Provides:       tex(OT1Montserrat-Inf.fd) = %{tl_version}
Provides:       tex(OT1Montserrat-LF.fd) = %{tl_version}
Provides:       tex(OT1Montserrat-Numr.fd) = %{tl_version}
Provides:       tex(OT1Montserrat-OsF.fd) = %{tl_version}
Provides:       tex(OT1Montserrat-Sup.fd) = %{tl_version}
Provides:       tex(OT1Montserrat-TLF.fd) = %{tl_version}
Provides:       tex(OT1Montserrat-TOsF.fd) = %{tl_version}
Provides:       tex(OT1MontserratAlternates-Dnom.fd) = %{tl_version}
Provides:       tex(OT1MontserratAlternates-Inf.fd) = %{tl_version}
Provides:       tex(OT1MontserratAlternates-LF.fd) = %{tl_version}
Provides:       tex(OT1MontserratAlternates-Numr.fd) = %{tl_version}
Provides:       tex(OT1MontserratAlternates-OsF.fd) = %{tl_version}
Provides:       tex(OT1MontserratAlternates-Sup.fd) = %{tl_version}
Provides:       tex(OT1MontserratAlternates-TLF.fd) = %{tl_version}
Provides:       tex(OT1MontserratAlternates-TOsF.fd) = %{tl_version}
Provides:       tex(T1Montserrat-Dnom.fd) = %{tl_version}
Provides:       tex(T1Montserrat-Inf.fd) = %{tl_version}
Provides:       tex(T1Montserrat-LF.fd) = %{tl_version}, tex(T1Montserrat-Numr.fd) = %{tl_version}
Provides:       tex(T1Montserrat-OsF.fd) = %{tl_version}
Provides:       tex(T1Montserrat-Sup.fd) = %{tl_version}
Provides:       tex(T1Montserrat-TLF.fd) = %{tl_version}
Provides:       tex(T1Montserrat-TOsF.fd) = %{tl_version}
Provides:       tex(T1MontserratAlternates-Dnom.fd) = %{tl_version}
Provides:       tex(T1MontserratAlternates-Inf.fd) = %{tl_version}
Provides:       tex(T1MontserratAlternates-LF.fd) = %{tl_version}
Provides:       tex(T1MontserratAlternates-Numr.fd) = %{tl_version}
Provides:       tex(T1MontserratAlternates-OsF.fd) = %{tl_version}
Provides:       tex(T1MontserratAlternates-Sup.fd) = %{tl_version}
Provides:       tex(T1MontserratAlternates-TLF.fd) = %{tl_version}
Provides:       tex(T1MontserratAlternates-TOsF.fd) = %{tl_version}
Provides:       tex(TS1Montserrat-LF.fd) = %{tl_version}
Provides:       tex(TS1Montserrat-OsF.fd) = %{tl_version}
Provides:       tex(TS1Montserrat-TLF.fd) = %{tl_version}
Provides:       tex(TS1Montserrat-TOsF.fd) = %{tl_version}
Provides:       tex(TS1MontserratAlternates-LF.fd) = %{tl_version}
Provides:       tex(TS1MontserratAlternates-OsF.fd) = %{tl_version}
Provides:       tex(TS1MontserratAlternates-TLF.fd) = %{tl_version}
Provides:       tex(TS1MontserratAlternates-TOsF.fd) = %{tl_version}

%description -n texlive-montserrat
Montserrat is a geometric sans-serif typeface designed by
Julieta Ulanovsky, inspired by posters and signage from her
historical Buenos Aires neighborhood of the same name. It is
rather close in spirit to Gotham and Proxima Nova, but has its
own individual appearance -- more informal, less extended, and
more idiosyncratic. It is provided in a total of nine different
weights, each having eight figure styles and small caps in both
upright and italic shapes. There are two quite different
versions that don't fit into the usual LaTeX classifications.
The version having the appellation "Alternates" has letter
shapes that are much more rounded than the default version,
reflecting the signage in the neighborhood of Montserrat.

%package -n texlive-mpostinl
Summary:        Embed MetaPost figures within LaTeX documents
Version:        svn46778
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(mpostinl.sty) = %{tl_version}

%description -n texlive-mpostinl
This LaTeX2e package enables the embedding of MetaPost figures
within LaTeX documents. The package automatically collects the
embedded definitions and figures in a .mp file, adds an
appropriate LaTeX document structure, and compiles it to .mps
files. It also allows for various configuration options to
manage the generation of files and compilation.

%package -n texlive-mucproc
Summary:        Conference proceedings for the German MuC-conference
Version:        svn43445
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(mucfontsize10pt.clo) = %{tl_version}
Provides:       tex(mucproc.cls) = %{tl_version}

%description -n texlive-mucproc
The mucproc.cls is a document class to support the formatting
guidelines for submissions to the German Mensch und Computer
conference. This work consists of the files mucproc.dtx and
mucproc.ins and the derived files mucproc.cls,
mucfontsize10pt.clo. A compilable demonstration file using the
mucproc class can be found on
https://github.com/Blubu/mucproc/. This example fulfills the
formatting guidelines for MuC 2017.

%package -n texlive-multilang
Summary:        A LaTeX package for maintaining multiple translations of a document
Version:        svn45179
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(multilang-sect.sty) = %{tl_version}, tex(multilang-tags.sty) = %{tl_version}
Provides:       tex(multilang.sty) = %{tl_version}

%description -n texlive-multilang
Maintaining a LaTeX document with translations for multiple
languages can be cumbersome and error-prone. This package
provides a set of macros for defining macros and environments
as wrappers around existing macros and environments. These
wrappers allow one to clearly specify multiple translations for
the arguments to the wrapped macros and environments while only
the translation of the document's language is actually shown.
Choosing a translation then is as simple as choosing the
document's language via babel or polyglossia.

%package -n texlive-musicography
Summary:        Accessing symbols for music writing with pdfLaTeX
Version:        svn47838
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(musicography.sty) = %{tl_version}

%description -n texlive-musicography
This package makes available the most commonly used symbols in
writing about music in a way that can be used with pdfLaTeX and
looks consistent and attractive. It includes accidentals,
meters, and notes of different rhythmic values. The package
builds on the approach used in the harmony package, where the
symbols are taken from the MusiXTeX fonts. But it provides a
larger range of symbols and a more flexible, user-friendly
interface written using xparse.

%package -n texlive-na-box
Summary:        Arabic-aware version of pas-cours package
Version:        svn45130
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(na-box.sty) = %{tl_version}

%description -n texlive-na-box
This is a modified version of the pas-cours package made
compatible with XeLaTeX/polyglossia to write arabic documents
with fancy boxed theorem-alike environments.

%package -n texlive-na-position
Summary:        Tables of relative positions of curves and asymptotes or tangents in Arabic documents
Version:        svn48071
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(na-position.sty) = %{tl_version}

%description -n texlive-na-position
This package facilitates, in most cases, the creation of tables
of relative positions of a curve and its asymptote, or a curve
and a tangent in one of its points. It depends on tkz-tab and
listofitems, as well as amsmath, amsfonts, mathrsfs, and
amssymb. This package has to be used with polyglossia and
XeLaTeX to produce documents in Arabic.

%package -n texlive-navydocs
Summary:        Support for Technical Reports by US Navy Organizations
Version:        svn41643
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(navydocs.sty) = %{tl_version}

%description -n texlive-navydocs
The navydocs package provides an easy means for creating title
pages and the following supplementary material pages used in
technical reports by United States Navy organizations. These
pages are generated by specifying the page content via a set of
commands and then calling a macro to create the page at its
occurence in the document. This package is provided in the hope
that it proves useful to other Navy organizations, with users
contributing macros for their organizations.

%package -n texlive-niceframe-type1
Summary:        Type 1 versions of the fonts recommended in niceframe
Version:        svn44671
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(niceframe.map) = %{tl_version}, tex(bbding10.pfb) = %{tl_version}
Provides:       tex(dingbat.pfb) = %{tl_version}, tex(karta15.pfb) = %{tl_version}
Provides:       tex(umranda.pfb) = %{tl_version}, tex(umrandb.pfb) = %{tl_version}

%description -n texlive-niceframe-type1
The bundle provides Adobe Type 1 versions of the fonts
bbding10, dingbat, karta15, umranda and umrandb.

%package -n texlive-modernposter
Summary:        A modern LaTeX poster theme
Version:        svn47269
License:        CC-BY-SA
Requires:       texlive-base texlive-kpathsea
Provides:       tex(modernposter.cls) = %{tl_version}

%description -n texlive-modernposter
This class extends the a0poster class in that it adds support
to easily create posters without the need for taking care of
the layout at all. It allows to use \maketitle to generate a
fancy header containing the title information and also provides
macros to position various different types of text boxes in a
two-column layout. The color scheme is inspired by the
metropolis beamer theme.

%package -n texlive-modulus
Summary:        A non-destructive modulus and integer quotient operator for TeX
Version:        svn47599
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(modulus.sty) = %{tl_version}

%description -n texlive-modulus
The package provides an easy way to take the remainder of a
division operation without destroying the values of the
counters containing the dividend and divisor. Also provides a
way to take the integer quotient of a division operation
without destroying the values of the counters containing the
dividend and divisor. A tiny but occasionally useful package,
when doing heavy TeX programming.

%package -n texlive-morisawa
Summary:        Enables selection of 5 standard Japanese fonts for pLaTeX + dvips
Version:        svn46946
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(morisawa5.map) = %{tl_version}, tex(FutoGoB101-Bold-H.tfm) = %{tl_version}
Provides:       tex(FutoGoB101-Bold-J.tfm) = %{tl_version}
Provides:       tex(FutoGoB101-Bold-V.tfm) = %{tl_version}
Provides:       tex(FutoMinA101-Bold-H.tfm) = %{tl_version}
Provides:       tex(FutoMinA101-Bold-J.tfm) = %{tl_version}
Provides:       tex(FutoMinA101-Bold-V.tfm) = %{tl_version}
Provides:       tex(GothicBBB-Medium-H.tfm) = %{tl_version}
Provides:       tex(GothicBBB-Medium-J.tfm) = %{tl_version}
Provides:       tex(GothicBBB-Medium-V.tfm) = %{tl_version}
Provides:       tex(Jun101-Light-H.tfm) = %{tl_version}, tex(Jun101-Light-J.tfm) = %{tl_version}
Provides:       tex(Jun101-Light-V.tfm) = %{tl_version}, tex(Ryumin-Light-H.tfm) = %{tl_version}
Provides:       tex(Ryumin-Light-J.tfm) = %{tl_version}, tex(Ryumin-Light-V.tfm) = %{tl_version}
Provides:       tex(futogo-b-v.tfm) = %{tl_version}, tex(futogo-b.tfm) = %{tl_version}
Provides:       tex(futomin-b-v.tfm) = %{tl_version}, tex(futomin-b.tfm) = %{tl_version}
Provides:       tex(gtbbb-m-v.tfm) = %{tl_version}, tex(gtbbb-m.tfm) = %{tl_version}
Provides:       tex(jun101-l-v.tfm) = %{tl_version}, tex(jun101-l.tfm) = %{tl_version}
Provides:       tex(ryumin-l-v.tfm) = %{tl_version}, tex(ryumin-l.tfm) = %{tl_version}
Provides:       tex(FutoGoB101-Bold-H.vf) = %{tl_version}
Provides:       tex(FutoGoB101-Bold-J.vf) = %{tl_version}
Provides:       tex(FutoGoB101-Bold-V.vf) = %{tl_version}
Provides:       tex(FutoMinA101-Bold-H.vf) = %{tl_version}
Provides:       tex(FutoMinA101-Bold-J.vf) = %{tl_version}
Provides:       tex(FutoMinA101-Bold-V.vf) = %{tl_version}
Provides:       tex(GothicBBB-Medium-H.vf) = %{tl_version}
Provides:       tex(GothicBBB-Medium-J.vf) = %{tl_version}
Provides:       tex(GothicBBB-Medium-V.vf) = %{tl_version}
Provides:       tex(Jun101-Light-H.vf) = %{tl_version}, tex(Jun101-Light-J.vf) = %{tl_version}
Provides:       tex(Jun101-Light-V.vf) = %{tl_version}, tex(Ryumin-Light-H.vf) = %{tl_version}
Provides:       tex(Ryumin-Light-J.vf) = %{tl_version}, tex(Ryumin-Light-V.vf) = %{tl_version}
Provides:       tex(morisawa.sty) = %{tl_version}

%description -n texlive-morisawa
The package enables selection of 5 standard Japanese fonts for
pLaTeX + dvips. It was originally written by Haruhiko Okumura
as part of jsclasses bundle, and the TFM/VF files were
previously distributed as part of the ptex-fonts package.

%package -n texlive-mptrees
Summary:        Probability trees with MetaPost
Version:        svn44453
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(mptrees.mp) = %{tl_version}

%description -n texlive-mptrees
This package provides MetaPost tools for drawing simple
probability trees. One command and several parameters to
control the output are provided.

%package -n texlive-musikui
Summary:        Easy creation of "arithmetical restoration" puzzles
Version:        svn47472
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(graphicx.sty)
Provides:       tex(musikui.sty) = %{tl_version}

%description -n texlive-musikui
This package permits to easily typeset arithmetical
longdesc restorations using LaTeX. This package requires the graphicx
longdesc package.

%package -n texlive-nicematrix
Summary:        Several features to improve the typesetting of mathematical matrices with TikZ
Version:        svn48395
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(nicematrix.sty) = %{tl_version}

%description -n texlive-nicematrix
This package provides new environments similar to the
environments matrix, pmatrix, bmatrix, etc. of amsmath and
mathtools. In these new environments, a TikZ node is created
for each cell of the matrix. The user can use these nodes
directly but nicematrix also provides commands which use these
nodes to draw continuous dotted lines from two cells of the
matrix (the result is more aesthetic than the classical result
obtained using \cdots, \vdots, \ddots, etc.). This package also
provides a control over the width of the columns and the
possibility to add an exterior line and an exterior column.

%package -n texlive-nidanfloat
Summary:        Bottom placement option for double float in two column mode (nidan-kumi)
Version:        svn48295
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(nidanfloat.sty) = %{tl_version}

%description -n texlive-nidanfloat
This package enables a bottom placement option for double
floats in two column mode (nidan-kumi). It was originally part
of the Japanese pLaTeX bundle and is now distributed as a
separate package because it supports all LaTeX formats.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/newpx"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*


%files -n texlive-natbib
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/natbib/
%{_texdir}/texmf-dist/tex/latex/natbib/

%files -n texlive-natbib-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/natbib/

%files -n texlive-multibib
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/multibib/
%{_texdir}/texmf-dist/makeindex/multibib/
%{_texdir}/texmf-dist/tex/latex/multibib/

%files -n texlive-multibib-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/multibib/

%files -n texlive-munich
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/munich/

%files -n texlive-munich-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/munich/

%files -n texlive-nar
%license other-free.txt
%{_texdir}/texmf-dist/bibtex/bst/nar/

%files -n texlive-nmbib
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/nmbib/
%{_texdir}/texmf-dist/tex/latex/nmbib/

%files -n texlive-nmbib-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/nmbib/

%files -n texlive-newpx
%license lppl1.txt
%{_datadir}/fonts/newpx
%{_texdir}/texmf-dist/fonts/afm/public/newpx/
%{_texdir}/texmf-dist/fonts/enc/dvips/newpx/
%{_texdir}/texmf-dist/fonts/map/dvips/newpx/
%{_texdir}/texmf-dist/fonts/opentype/public/newpx/
%{_texdir}/texmf-dist/fonts/tfm/public/newpx/
%{_texdir}/texmf-dist/fonts/type1/public/newpx/
%{_texdir}/texmf-dist/fonts/vf/public/newpx/
%{_texdir}/texmf-dist/tex/latex/newpx/

%files -n texlive-newpx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/newpx/

%files -n texlive-newtx
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/afm/public/newtx/
%{_texdir}/texmf-dist/fonts/enc/dvips/newtx/
%{_texdir}/texmf-dist/fonts/map/dvips/newtx/
%{_texdir}/texmf-dist/fonts/opentype/public/newtx/
%{_texdir}/texmf-dist/fonts/tfm/public/newtx/
%{_texdir}/texmf-dist/fonts/type1/public/newtx/
%{_texdir}/texmf-dist/fonts/vf/public/newtx/
%{_texdir}/texmf-dist/tex/latex/newtx/

%files -n texlive-newtx-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/newtx/

%files -n texlive-newtxsf
%license ofl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/newtxsf/
%{_texdir}/texmf-dist/fonts/tfm/public/newtxsf/
%{_texdir}/texmf-dist/fonts/type1/public/newtxsf/
%{_texdir}/texmf-dist/fonts/vf/public/newtxsf/
%{_texdir}/texmf-dist/tex/latex/newtxsf/

%files -n texlive-newtxsf-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/newtxsf/

%files -n texlive-newtxtt
%license gpl3.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/newtxtt/
%{_texdir}/texmf-dist/fonts/map/dvips/newtxtt/
%{_texdir}/texmf-dist/fonts/tfm/public/newtxtt/
%{_texdir}/texmf-dist/fonts/type1/public/newtxtt/
%{_texdir}/texmf-dist/tex/latex/newtxtt/

%files -n texlive-newtxtt-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/fonts/newtxtt/

%files -n texlive-nkarta
%license pd.txt
%{_texdir}/texmf-dist/fonts/source/public/nkarta/
%{_texdir}/texmf-dist/fonts/tfm/public/nkarta/
%{_texdir}/texmf-dist/metapost/nkarta/

%files -n texlive-nkarta-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/nkarta/

%files -n texlive-ncntrsbk
%license gpl.txt
%{_texdir}/texmf-dist/dvips/ncntrsbk/
%{_texdir}/texmf-dist/fonts/afm/adobe/ncntrsbk/
%{_texdir}/texmf-dist/fonts/afm/urw/ncntrsbk/
%{_texdir}/texmf-dist/fonts/map/dvips/ncntrsbk/
%{_texdir}/texmf-dist/fonts/tfm/adobe/ncntrsbk/
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/ncntrsbk/
%{_texdir}/texmf-dist/fonts/type1/urw/ncntrsbk/
%{_texdir}/texmf-dist/fonts/vf/adobe/ncntrsbk/
%{_texdir}/texmf-dist/fonts/vf/urw35vf/ncntrsbk/
%{_texdir}/texmf-dist/tex/latex/ncntrsbk/

%files -n texlive-navigator
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/navigator/

%files -n texlive-navigator-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/navigator/

%files -n texlive-multido
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/multido/
%{_texdir}/texmf-dist/tex/latex/multido/

%files -n texlive-multido-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/multido/

%files -n texlive-ncctools
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ncctools/

%files -n texlive-ncctools-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ncctools/

%files -n texlive-mongolian-babel
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mongolian-babel/

%files -n texlive-mongolian-babel-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mongolian-babel/

%files -n texlive-montex
%license gpl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/montex/
%{_texdir}/texmf-dist/fonts/source/public/montex/
%{_texdir}/texmf-dist/fonts/tfm/public/montex/
%{_texdir}/texmf-dist/fonts/type1/public/montex/
%{_texdir}/texmf-dist/tex/latex/montex/

%files -n texlive-montex-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/montex/

%files -n texlive-mpman-ru-doc
%{_texdir}/texmf-dist/doc/metapost/mpman-ru/

%files -n texlive-nevelok
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/nevelok/

%files -n texlive-nevelok-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/nevelok/

%files -n texlive-nanumtype1
%license ofl.txt
%{_texdir}/texmf-dist/fonts/afm/public/nanumtype1/
%{_texdir}/texmf-dist/fonts/map/dvips/nanumtype1/
%{_texdir}/texmf-dist/fonts/tfm/public/nanumtype1/
%{_texdir}/texmf-dist/fonts/type1/public/nanumtype1/
%{_texdir}/texmf-dist/fonts/vf/public/nanumtype1/
%{_texdir}/texmf-dist/tex/latex/nanumtype1/

%files -n texlive-nanumtype1-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/nanumtype1/

%files -n texlive-mwcls
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mwcls/

%files -n texlive-mwcls-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mwcls/

%files -n texlive-ms
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ms/

%files -n texlive-ms-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ms/

%files -n texlive-modiagram
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/modiagram/

%files -n texlive-modiagram-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/modiagram/

%files -n texlive-neuralnetwork
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/neuralnetwork/

%files -n texlive-neuralnetwork-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/neuralnetwork/

%files -n texlive-moderncv
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/moderncv/

%files -n texlive-moderncv-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/moderncv/

%files -n texlive-moderntimeline
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/moderntimeline/

%files -n texlive-moderntimeline-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/moderntimeline/

%files -n texlive-modref
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/modref/

%files -n texlive-modref-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/modref/

%files -n texlive-modroman
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/modroman/

%files -n texlive-modroman-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/modroman/

%files -n texlive-monofill
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/monofill/

%files -n texlive-monofill-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/monofill/

%files -n texlive-moreenum
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/moreenum/

%files -n texlive-moreenum-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/moreenum/

%files -n texlive-morefloats
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/morefloats/

%files -n texlive-morefloats-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/morefloats/

%files -n texlive-morehype
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/morehype/

%files -n texlive-morehype-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/morehype/

%files -n texlive-moresize
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/moresize/

%files -n texlive-moresize-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/moresize/

%files -n texlive-moreverb
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/moreverb/

%files -n texlive-moreverb-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/moreverb/

%files -n texlive-morewrites
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/morewrites/

%files -n texlive-morewrites-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/morewrites/

%files -n texlive-mparhack
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/mparhack/

%files -n texlive-mparhack-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/mparhack/

%files -n texlive-msc
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bib/msc/
%{_texdir}/texmf-dist/tex/latex/msc/

%files -n texlive-msc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/msc/

%files -n texlive-msg
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/msg/

%files -n texlive-msg-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/msg/

%files -n texlive-mslapa
%{_texdir}/texmf-dist/bibtex/bst/mslapa/
%{_texdir}/texmf-dist/tex/latex/mslapa/

%files -n texlive-mslapa-doc
%{_texdir}/texmf-dist/doc/latex/mslapa/

%files -n texlive-mtgreek
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mtgreek/

%files -n texlive-mtgreek-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mtgreek/

%files -n texlive-multenum
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/multenum/

%files -n texlive-multenum-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/multenum/

%files -n texlive-multiaudience
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/multiaudience/

%files -n texlive-multiaudience-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/multiaudience/

%files -n texlive-multibbl
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/multibbl/

%files -n texlive-multibbl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/multibbl/

%files -n texlive-multicap
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/multicap/

%files -n texlive-multicap-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/multicap/

%files -n texlive-multienv
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/multienv/

%files -n texlive-multienv-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/multienv/

%files -n texlive-multiexpand
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/multiexpand/

%files -n texlive-multiexpand-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/multiexpand/

%files -n texlive-multirow
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/multirow/

%files -n texlive-multirow-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/multirow/

%files -n texlive-mversion
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/mversion/

%files -n texlive-mversion-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/mversion/

%files -n texlive-mwe
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mwe/

%files -n texlive-mwe-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mwe/

%files -n texlive-mweights
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/mweights/

%files -n texlive-mweights-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/mweights/

%files -n texlive-mycv
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/mycv/
%{_texdir}/texmf-dist/tex/latex/mycv/

%files -n texlive-mycv-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mycv/

%files -n texlive-mylatexformat
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mylatexformat/

%files -n texlive-mylatexformat-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mylatexformat/

%files -n texlive-nag
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/nag/

%files -n texlive-nag-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nag/

%files -n texlive-nameauth
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/nameauth/

%files -n texlive-nameauth-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/nameauth/

%files -n texlive-namespc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/namespc/

%files -n texlive-namespc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/namespc/

%files -n texlive-ncclatex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ncclatex/

%files -n texlive-ncclatex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ncclatex/

%files -n texlive-needspace
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/needspace/

%files -n texlive-needspace-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/needspace/

%files -n texlive-nestquot
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/nestquot/

%files -n texlive-newcommand-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/newcommand/

%files -n texlive-newenviron
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/newenviron/

%files -n texlive-newenviron-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/newenviron/

%files -n texlive-newfile
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/newfile/

%files -n texlive-newfile-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/newfile/

%files -n texlive-newlfm
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/newlfm/

%files -n texlive-newlfm-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/newlfm/

%files -n texlive-newspaper
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/newspaper/

%files -n texlive-newspaper-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/newspaper/

%files -n texlive-newunicodechar
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/newunicodechar/

%files -n texlive-newunicodechar-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/newunicodechar/

%files -n texlive-newvbtm
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/newvbtm/

%files -n texlive-newvbtm-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/newvbtm/

%files -n texlive-newverbs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/newverbs/

%files -n texlive-newverbs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/newverbs/

%files -n texlive-nextpage
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/nextpage/

%files -n texlive-nfssext-cfr
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/nfssext-cfr/

%files -n texlive-nfssext-cfr-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/nfssext-cfr/

%files -n texlive-nicefilelist
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/nicefilelist/

%files -n texlive-nicefilelist-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/nicefilelist/

%files -n texlive-niceframe
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/niceframe/
%{_texdir}/texmf-dist/fonts/tfm/public/niceframe/
%{_texdir}/texmf-dist/tex/latex/niceframe/

%files -n texlive-niceframe-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/niceframe/

%files -n texlive-nicetext
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/nicetext/

%files -n texlive-nicetext-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nicetext/

%files -n texlive-nlctdoc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/nlctdoc/

%files -n texlive-nlctdoc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nlctdoc/

%files -n texlive-multiobjective
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/multiobjective/

%files -n texlive-multiobjective-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/multiobjective/

%files -n texlive-natded
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/natded/

%files -n texlive-natded-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/natded/

%files -n texlive-nath
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/nath/

%files -n texlive-nath-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/nath/

%files -n texlive-mp3d
%{_texdir}/texmf-dist/metapost/mp3d/

%files -n texlive-mp3d-doc
%{_texdir}/texmf-dist/doc/metapost/mp3d/

%files -n texlive-mpcolornames
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/mpcolornames/

%files -n texlive-mpcolornames-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/mpcolornames/

%files -n texlive-mpattern
%license pd.txt
%{_texdir}/texmf-dist/metapost/mpattern/

%files -n texlive-mpattern-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/metapost/mpattern/

%files -n texlive-mpgraphics
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mpgraphics/

%files -n texlive-mpgraphics-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mpgraphics/

%files -n texlive-musixguit
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/musixguit/

%files -n texlive-musixguit-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/musixguit/

%files -n texlive-musixtex-fonts
%license gpl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/musixtex-fonts/
%{_texdir}/texmf-dist/fonts/source/public/musixtex-fonts/
%{_texdir}/texmf-dist/fonts/tfm/public/musixtex-fonts/
%{_texdir}/texmf-dist/fonts/type1/public/musixtex-fonts/

%files -n texlive-musixtex-fonts-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/musixtex-fonts/

%files -n texlive-mxedruli
%{_texdir}/texmf-dist/fonts/afm/public/mxedruli/
%{_texdir}/texmf-dist/fonts/map/dvips/mxedruli/
%{_texdir}/texmf-dist/fonts/source/public/mxedruli/
%{_texdir}/texmf-dist/fonts/tfm/public/mxedruli/
%{_texdir}/texmf-dist/fonts/type1/public/mxedruli/
%{_texdir}/texmf-dist/tex/latex/mxedruli/

%files -n texlive-mxedruli-doc
%{_texdir}/texmf-dist/doc/fonts/mxedruli/

%files -n texlive-newsletr
%{_texdir}/texmf-dist/tex/plain/newsletr/

%files -n texlive-newsletr-doc
%{_texdir}/texmf-dist/doc/plain/newsletr/

%files -n texlive-msu-thesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/msu-thesis/

%files -n texlive-msu-thesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/msu-thesis/

%files -n texlive-mugsthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mugsthesis/

%files -n texlive-mugsthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mugsthesis/

%files -n texlive-musuos
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/musuos/

%files -n texlive-musuos-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/musuos/

%files -n texlive-muthesis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/muthesis/

%files -n texlive-muthesis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/muthesis/

%files -n texlive-nature
%{_texdir}/texmf-dist/bibtex/bst/nature/
%{_texdir}/texmf-dist/tex/latex/nature/

%files -n texlive-nature-doc
%{_texdir}/texmf-dist/doc/latex/nature/

%files -n texlive-nddiss
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/nddiss/
%{_texdir}/texmf-dist/tex/latex/nddiss/

%files -n texlive-nddiss-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nddiss/

%files -n texlive-ndsu-thesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ndsu-thesis/

%files -n texlive-ndsu-thesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ndsu-thesis/

%files -n texlive-nih
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/nih/

%files -n texlive-nih-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/nih/

%files -n texlive-mychemistry
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/mychemistry/

%files -n texlive-mychemistry-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/mychemistry/

%files -n texlive-moodle-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/moodle/

%files -n texlive-moodle
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/moodle/

%files -n texlive-mparrows-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/metapost/mparrows/

%files -n texlive-mparrows
%license pd.txt
%{_texdir}/texmf-dist/metapost/mparrows/

%files -n texlive-multidef-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/multidef/

%files -n texlive-multidef
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/multidef/

%files -n texlive-mynsfc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/xelatex/mynsfc/

%files -n texlive-mynsfc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/xelatex/mynsfc/

%files -n texlive-nihbiosketch-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/nihbiosketch/

%files -n texlive-nihbiosketch
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/nihbiosketch/

%files -n texlive-nimbus15-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/fonts/nimbus15/

%files -n texlive-nimbus15
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/nimbus15/
%{_texdir}/texmf-dist/fonts/opentype/public/nimbus15/
%{_texdir}/texmf-dist/fonts/map/dvips/nimbus15/
%{_texdir}/texmf-dist/fonts/tfm/public/nimbus15/
%{_texdir}/texmf-dist/fonts/vf/public/nimbus15/
%{_texdir}/texmf-dist/fonts/enc/dvips/nimbus15/
%{_texdir}/texmf-dist/fonts/afm/public/nimbus15/
%{_texdir}/texmf-dist/fonts/type1/public/nimbus15/

%files -n texlive-modular
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/modular/
%{_texdir}/texmf-dist/tex/latex/modular/

%files -n texlive-montserrat
%license ofl.txt lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/fonts/montserrat/
%{_texdir}/texmf-dist/fonts/enc/dvips/montserrat/
%{_texdir}/texmf-dist/fonts/map/dvips/montserrat/
%{_texdir}/texmf-dist/fonts/opentype/public/montserrat/
%{_texdir}/texmf-dist/fonts/tfm/public/montserrat/
%{_texdir}/texmf-dist/fonts/type1/public/montserrat/
%{_texdir}/texmf-dist/fonts/vf/public/montserrat/
%{_texdir}/texmf-dist/tex/latex/montserrat/

%files -n texlive-mpostinl
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/mpostinl/
%{_texdir}/texmf-dist/tex/latex/mpostinl/

%files -n texlive-mucproc
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/mucproc/
%{_texdir}/texmf-dist/tex/latex/mucproc/

%files -n texlive-multilang
%license lppl1.2.txt
%doc %{_texdir}/texmf-dist/doc/latex/multilang/
%{_texdir}/texmf-dist/tex/latex/multilang/

%files -n texlive-musicography
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/musicography/
%{_texdir}/texmf-dist/tex/latex/musicography/

%files -n texlive-na-box
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/xelatex/na-box/
%{_texdir}/texmf-dist/tex/xelatex/na-box/

%files -n texlive-na-position
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/xelatex/na-position/
%{_texdir}/texmf-dist/tex/xelatex/na-position/

%files -n texlive-navydocs
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/navydocs/
%{_texdir}/texmf-dist/tex/latex/navydocs/

%files -n texlive-niceframe-type1
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/fonts/niceframe-type1/
%{_texdir}/texmf-dist/fonts/afm/public/niceframe-type1/
%{_texdir}/texmf-dist/fonts/map/dvips/niceframe-type1/
%{_texdir}/texmf-dist/fonts/type1/public/niceframe-type1/

%files -n texlive-modernposter
%{_texdir}/texmf-dist/tex/latex/modernposter/
%doc %{_texdir}/texmf-dist/doc/latex/modernposter/

%files -n texlive-modulus
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/generic/modulus/
%{_texdir}/texmf-dist/tex/generic/modulus/


%files -n texlive-morisawa
%license bsd.txt
%{_texdir}/texmf-dist/fonts/map/dvipdfmx/morisawa/
%{_texdir}/texmf-dist/fonts/tfm/public/morisawa/
%{_texdir}/texmf-dist/fonts/vf/public/morisawa/
%{_texdir}/texmf-dist/tex/latex/morisawa/
%doc %{_texdir}/texmf-dist/doc/fonts/morisawa/

%files -n texlive-mptrees
%license lppl.txt
%{_texdir}/texmf-dist/metapost/mptrees/
%doc %{_texdir}/texmf-dist/doc/metapost/mptrees/

%files -n texlive-musikui
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/musikui/
%doc %{_texdir}/texmf-dist/doc/latex/musikui/

%files -n texlive-nicematrix
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/nicematrix/
%doc %{_texdir}/texmf-dist/doc/latex/nicematrix/

%files -n texlive-nidanfloat
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/nidanfloat/
%doc %{_texdir}/texmf-dist/doc/latex/nidanfloat/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
