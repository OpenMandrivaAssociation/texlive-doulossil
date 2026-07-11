%global tl_name doulossil
%global tl_revision 63255

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	A font for typesetting the International Phonetic Alphabet (IPA)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/doulossil
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/doulossil.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/doulossil.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the IPA font Doulos SIL in TrueType format.

