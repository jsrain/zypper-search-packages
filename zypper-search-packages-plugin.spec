#
# spec file for package zypper-search-packages-plugin
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           zypper-search-packages-plugin
Version:        0.3
Release:        0
Summary:        Zypper subcommand for online package search
License:        GPL-2.0-only
Group:          System/Packages
URL:            https://github.com/jsrain/zypper-search-packages
Source0:        zypper-search-packages-git.tar.xz
BuildRequires:  ruby-macros >= 5
BuildRequires:  zypper >= 1.11.38
Requires:       zypper >= 1.11.38
Requires:       rubygem(%{rb_default_ruby_abi}:suse-connect) >= 0.3.9
Supplements:    packageand(zypper:SUSEConnect)
Obsoletes:	zypper-package-search-plugin
BuildArch:      noarch

%description
Zypper subcommand for online package search via
the API of the SUSE Customer Center.

%prep
%setup -q -n zypper-search-packages-git

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/zypper/commands
install -m 755 zypper-search-packages %{buildroot}%{_prefix}/lib/zypper/commands/

%files
%license COPYING
%{_prefix}/lib/zypper/commands

%changelog
