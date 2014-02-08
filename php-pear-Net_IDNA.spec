%define		_class		Net
%define		_subclass	IDNA
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.8.1
Release:	5
Summary:	Punycode encoding and decoding
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_IDNA/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This package helps you to encode and decode punycode strings easily.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-3mdv2012.0
+ Revision: 741793
- fix major breakage by careless packager

* Thu Dec 15 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-2
+ Revision: 741509
- rebuilt to see if it makes it to main..., phew!

* Wed Dec 14 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1
+ Revision: 741265
- 0.8.1

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-7
+ Revision: 679417
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-6mdv2011.0
+ Revision: 613727
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.1-5mdv2010.1
+ Revision: 468702
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.7.1-4mdv2010.0
+ Revision: 441449
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-3mdv2009.1
+ Revision: 322416
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-2mdv2009.0
+ Revision: 236984
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.7.1-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-1mdv2007.0
+ Revision: 82314
- Import php-pear-Net_IDNA

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-1mdk
- 0.7.1
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-5mdk
- fix deps

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-4mdk
- fix the package.xml file so it will register

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-1mdk
- initial Mandriva package (PLD import)

