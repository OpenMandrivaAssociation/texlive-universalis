%global tl_name universalis
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Universalis font, with support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/universalis
License:	gpl2+ lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/universalis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/universalis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the UniversalisADFStd family of fonts, designed by Hirwin Harendal. The
font is suitable as an alternative to fonts such as Adrian Frutiger's
Univers and Frutiger.

