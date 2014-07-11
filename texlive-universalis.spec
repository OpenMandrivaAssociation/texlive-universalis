# revision 33860
# category Package
# catalog-ctan /fonts/universalis
# catalog-date 2014-05-05 17:01:15 +0200
# catalog-license gpl2
# catalog-version undef
Name:		texlive-universalis
Version:	20140505
Release:	2
Summary:	Universalis font, with support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/universalis
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/universalis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/universalis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the UniversalisADFStd family of fonts, designed by
Hirwin Harendal. The font is suitable as an alternative to
fonts such as Adrian Frutiger's Univers and Frutiger.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/universalis/unvsl_fe7xck.enc
%{_texmfdistdir}/fonts/enc/dvips/universalis/unvsl_qu6a6x.enc
%{_texmfdistdir}/fonts/enc/dvips/universalis/unvsl_sjpjw4.enc
%{_texmfdistdir}/fonts/enc/dvips/universalis/unvsl_xtabpf.enc
%{_texmfdistdir}/fonts/map/dvips/universalis/universalis.map
%{_texmfdistdir}/fonts/opentype/arkandis/universalis/UniversalisADFStd-Bold.otf
%{_texmfdistdir}/fonts/opentype/arkandis/universalis/UniversalisADFStd-BoldCond.otf
%{_texmfdistdir}/fonts/opentype/arkandis/universalis/UniversalisADFStd-BoldCondIt.otf
%{_texmfdistdir}/fonts/opentype/arkandis/universalis/UniversalisADFStd-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/universalis/UniversalisADFStd-Cond.otf
%{_texmfdistdir}/fonts/opentype/arkandis/universalis/UniversalisADFStd-CondItalic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/universalis/UniversalisADFStd-Italic.otf
%{_texmfdistdir}/fonts/opentype/arkandis/universalis/UniversalisADFStd-Regular.otf
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCond-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCond-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCond-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCond-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCond-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCond-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCond-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCond-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCond-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCond-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCond-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Cond-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Cond-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Cond-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Cond-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Cond-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Cond-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Cond-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Cond-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Cond-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Cond-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Cond-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-CondItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-CondItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-CondItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-CondItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-CondItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-CondItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-CondItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-CondItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-CondItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-CondItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-CondItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/universalis/UniversalisADFStd-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-Bold.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-BoldCond.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-BoldCondIt.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-BoldCondItLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-BoldCondLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-BoldItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-BoldLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-Cond.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-CondItalic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-CondItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-CondLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-Italic.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-ItalicLCDFJ.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-Regular.pfb
%{_texmfdistdir}/fonts/type1/arkandis/universalis/UniversalisADFStd-RegularLCDFJ.pfb
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldCond-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldCond-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldCond-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldCond-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldCondIt-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Cond-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Cond-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Cond-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Cond-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-CondItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-CondItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-CondItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-CondItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/universalis/UniversalisADFStd-Regular-lf-ts1.vf
%{_texmfdistdir}/tex/latex/universalis/LY1UniversalisADFStd-LF.fd
%{_texmfdistdir}/tex/latex/universalis/OT1UniversalisADFStd-LF.fd
%{_texmfdistdir}/tex/latex/universalis/T1UniversalisADFStd-LF.fd
%{_texmfdistdir}/tex/latex/universalis/TS1UniversalisADFStd-LF.fd
%{_texmfdistdir}/tex/latex/universalis/UniversalisADFStd.sty
%{_texmfdistdir}/tex/latex/universalis/universalis.sty
%doc %{_texmfdistdir}/doc/fonts/universalis/COPYING
%doc %{_texmfdistdir}/doc/fonts/universalis/NOTICE.txt
%doc %{_texmfdistdir}/doc/fonts/universalis/README
%doc %{_texmfdistdir}/doc/fonts/universalis/universalis-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/universalis/universalis-samples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
