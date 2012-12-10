%define name dekagen
%define version 1.0.2
%define release 6

Summary:   Rips and encodes CD's
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    %{name}-%{version}.tar.bz2
License:   GPLv2+
Group:     Sound
# looks like is a dead end , maybe abbandon 
URL:       http://userpage.fu-berlin.de/~mbayer/tools/dekagen.html
Obsoletes: ripenc
Provides:  ripenc
Buildarch: noarch
BuildRequires: dos2unix

%description
The dekagen bourne shell script, formerly known as ripenc, is an interactive 
command line tool, that automates the whole process of ripping data from 
music compact discs (CD), the naming of the files, their converting 
into MP3 or Ogg-Vorbis format and the labelling of the MP3 files 
with an ID3 tag.

%prep
%setup 
#fix CRLF in CHANGES
cp --preserve CHANGES CHANGES.msdos
dos2unix  CHANGES
#fix utf8 encoding
iconv -f latin1 -t utf8 README > README 

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1

cp dekagen ${RPM_BUILD_ROOT}%{_bindir}
gunzip dekagen.1.gz
cp dekagen.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/


%files
%doc COPYING CHANGES INSTALL CREDITS README
%_bindir/*
%_mandir/man1/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6mdv2011.0
+ Revision: 617527
- the mass rebuild of 2010.0 packages

* Wed May 20 2009 Jérôme Brenier <incubusss@mandriva.org> 1.0.2-5mdv2010.0
+ Revision: 377891
- fix CRLF in CHANGES
- add a BR on dos2unix
- fix license (GPLv2+)

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2009.0
+ Revision: 244026
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2008.1
+ Revision: 123762
- kill re-definition of %%buildroot on Pixel's request
- import dekagen


* Tue Jan 03 2006 Lenny Cartier <lenny@mandriva.com> 1.0.2-2mdk
- rebuild

* Mon Jul 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-1mdk
- 1.0.2

* Mon Jan 12 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- 1.0.1

* Fri Oct 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0-1mdk
- new
- obsoletes ripenc
