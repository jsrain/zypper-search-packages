#
# spec file for package zypper-package-search
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           zypper-package-search-plugin
Version:        0.1
Release:        0
Requires:       rubygem(%{rb_default_ruby_abi}:suse-connect) >= 0.3.9
Requires:       zypper >= 1.11.38
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  zypper >= 1.11.38
Source1:        zypper-package-search
Source2:        COPYING
Summary:        Zypper subcommand for online package search
License:        GPL-2.0
Group:          System/Packages
BuildArch:      noarch
Supplements:    packageand(zypper:SUSEConnect)

%description
Zypper subcommand for online package search.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/zypper/commands
install -m 755 %{S:1} $RPM_BUILD_ROOT/usr/lib/zypper/commands/
install -d ${RPM_BUILD_ROOT}%{_defaultlicensedir}/%{name}
install -m 644 %{S:2} ${RPM_BUILD_ROOT}%{_defaultlicensedir}/%{name}

%files
%defattr(-,root,root,-)
/usr/lib/zypper/commands
%license COPYING

%changelog
