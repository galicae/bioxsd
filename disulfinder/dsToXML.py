

<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>bioxsd/disulfinder/dsToXML.py at master · galicae/bioxsd</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://a248.e.akamai.net/assets.github.com/images/modules/logos_page/Octocat.png">
    <link rel="assets" href="https://a248.e.akamai.net/assets.github.com/">
    <link rel="xhr-socket" href="/_sockets" />
    
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="1651067" name="octolytics-actor-id" /><meta content="galicae" name="octolytics-actor-login" /><meta content="d3fb6f72299428c1493803649702abdf2afe8e10ee91f85e9c6c4a5fd3d87c27" name="octolytics-actor-hash" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="TQq8/JYS7XYwFcmdSEY8ZQG7jDuE12K+flPCuzhDpIo=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-619a349a96b51920d29d7f36c58bdbb00074b712.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-e0e9c2910d8092b08fac19c6d89b0003ffc198e1.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-1f72571b966545f4e27481a3b0ebbeeed4f2f139.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-3b51dd74a94c713c22309e373955e5fa02a3bb65.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="4df5905436cb7c8f0e7c59b481e2afe5">

        <link data-pjax-transient rel='permalink' href='/galicae/bioxsd/blob/7e82b5c7f036fb7ed414e2180cf36714122785e1/disulfinder/dsToXML.py'>

  <meta property="og:title" content="bioxsd"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/galicae/bioxsd"/>
  <meta property="og:image" content="https://a248.e.akamai.net/assets.github.com/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="bioxsd - a repository for all things bioXSD (The Bioinformatics Lab 2013, TU Munich)"/>

  <meta name="description" content="bioxsd - a repository for all things bioXSD (The Bioinformatics Lab 2013, TU Munich)" />

  <meta content="1651067" name="octolytics-dimension-user_id" /><meta content="galicae" name="octolytics-dimension-user_login" /><meta content="10497809" name="octolytics-dimension-repository_id" /><meta content="galicae/bioxsd" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="10497809" name="octolytics-dimension-repository_network_root_id" /><meta content="galicae/bioxsd" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/galicae/bioxsd/commits/master.atom" rel="alternate" title="Recent Commits to bioxsd:master" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob linux vis-public env-production  kill-the-chrome">

    <div class="wrapper">
      
      
      

      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    <div class="divider-vertical"></div>

      <a href="/notifications" class="notification-indicator tooltipped downwards" title="You have no unread notifications">
    <span class="mail-status all-read"></span>
  </a>
  <div class="divider-vertical"></div>


      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="galicae"
      data-repo="galicae/bioxsd"
      data-branch="master"
      data-sha="f31862c1b5aa7227c7b2f223b413f08136be7e76"
  >

    <input type="hidden" name="nwo" value="galicae/bioxsd" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
            <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    

  

    <ul id="user-links">
      <li>
        <a href="/galicae" class="name">
          <img height="20" src="https://secure.gravatar.com/avatar/f21e60d0bcf9d88d6622d1ef83fb4e8d?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /> galicae
        </a>
      </li>

        <li>
          <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo">
            <span class="octicon octicon-repo-create"></span>
          </a>
        </li>

        <li>
          <a href="/settings/profile" id="account_settings"
            class="tooltipped downwards"
            title="Account settings ">
            <span class="octicon octicon-tools"></span>
          </a>
        </li>
        <li>
          <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out">
            <span class="octicon octicon-log-out"></span>
          </a>
        </li>

    </ul>


<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-list-unordered"></span> New organization</a>
  </li>



    <li class="section-title">
      <span title="galicae/bioxsd">This repository</span>
    </li>
    <li>
      <a href="/galicae/bioxsd/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>
      <li>
        <a href="/galicae/bioxsd/settings/collaboration"><span class="octicon octicon-person-add"></span> New collaborator</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

      




          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="TQq8/JYS7XYwFcmdSEY8ZQG7jDuE12K+flPCuzhDpIo=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="10497809" />

    <div class="select-menu js-menu-container js-select-menu">
      <span class="minibutton select-menu-button  js-menu-target">
        <span class="js-select-button">
          <span class="octicon octicon-eye-unwatch"></span>
          Unwatch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container">

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

    <li class="js-toggler-container js-social-container starring-container ">
      <a href="/galicae/bioxsd/unstar" class="minibutton with-count js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="octicon octicon-star-delete"></span>
        <span class="text">Unstar</span>
      </a>
      <a href="/galicae/bioxsd/star" class="minibutton with-count js-toggler-target star-button unstarred upwards" title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
        <span class="octicon octicon-star"></span>
        <span class="text">Star</span>
      </a>
      <a class="social-count js-social-count" href="/galicae/bioxsd/stargazers">1</a>
    </li>

        <li>
          <a href="/galicae/bioxsd/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="nofollow" data-method="post">
            <span class="octicon octicon-git-branch-create"></span>
            <span class="text">Fork</span>
          </a>
          <a href="/galicae/bioxsd/network" class="social-count">0</a>
        </li>


</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/galicae" class="url fn" itemprop="url" rel="author"><span itemprop="title">galicae</span></a></span
          ><span class="repohead-name-divider">/</span><strong
          ><a href="/galicae/bioxsd" class="js-current-repository js-repo-home-link">bioxsd</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">

      <div class="repository-with-sidebar repo-container
            ">

          <div class="repository-sidebar">

              

<div class="repo-nav repo-nav-full js-repository-container-pjax js-octicon-loaders">
  <div class="repo-nav-contents">
    <ul class="repo-menu">
      <li class="tooltipped leftwards" title="Code">
        <a href="/galicae/bioxsd" class="js-selected-navigation-item selected" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /galicae/bioxsd">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/galicae/bioxsd/issues" class="js-selected-navigation-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /galicae/bioxsd/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>1</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests"><a href="/galicae/bioxsd/pulls" class="js-selected-navigation-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /galicae/bioxsd/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped leftwards" title="Wiki">
          <a href="/galicae/bioxsd/wiki" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_wiki /galicae/bioxsd/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>


    </ul>
    <div class="repo-menu-separator"></div>
    <ul class="repo-menu">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/galicae/bioxsd/pulse" class="js-selected-navigation-item " data-pjax="true" data-selected-links="pulse /galicae/bioxsd/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/galicae/bioxsd/graphs" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_graphs repo_contributors /galicae/bioxsd/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/galicae/bioxsd/network" class="js-selected-navigation-item js-disable-pjax" data-selected-links="repo_network /galicae/bioxsd/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    </ul>

      <div class="repo-menu-separator"></div>
      <ul class="repo-menu">
        <li class="tooltipped leftwards" title="Settings">
          <a href="/galicae/bioxsd/settings" data-pjax>
            <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </a>
        </li>
      </ul>
  </div>
</div>


              <div class="only-with-full-nav">

                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=push">
  <h3><strong>HTTPS</strong> clone URL</h3>

  <input type="text" class="clone js-url-field"
         value="https://github.com/galicae/bioxsd.git" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/galicae/bioxsd.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push">
  <h3><strong>SSH</strong> clone URL</h3>

  <input type="text" class="clone js-url-field"
         value="git@github.com:galicae/bioxsd.git" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="git@github.com:galicae/bioxsd.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=push">
  <h3><strong>Subversion</strong> checkout URL</h3>

  <input type="text" class="clone js-url-field"
         value="https://github.com/galicae/bioxsd" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/galicae/bioxsd" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>



<p class="clone-options">You can clone with
    <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
    <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
    <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>,
  and <a href="https://help.github.com/articles/which-remote-url-should-i-use">other methods.</a>
</p>




                  <a href="/galicae/bioxsd/archive/master.zip"
                     class="minibutton sidebar-button"
                     title="Download this repository as a zip file"
                     rel="nofollow">
                    <span class="octicon octicon-cloud-download"></span>
                    Download ZIP
                  </a>

              </div>
          </div>

          <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
            


<!-- blob contrib key: blob_contributors:v21:e90a97de673ba07706dc2978d9f3e526 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:e90a97de673ba07706dc2978d9f3e526 -->


      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <a href="/galicae/bioxsd/find/master" data-pjax data-hotkey="t" style="display:none">Show File Finder</a>

        <div class="file-navigation">
          


<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/galicae/bioxsd/blob/master/disulfinder/dsToXML.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <form accept-charset="UTF-8" action="/galicae/bioxsd/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="TQq8/JYS7XYwFcmdSEY8ZQG7jDuE12K+flPCuzhDpIo=" /></div>
            <span class="octicon octicon-git-branch-create select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <h4>Create branch: <span class="js-new-item-name"></span></h4>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master" />
            <input type="hidden" name="path" id="branch" value="disulfinder/dsToXML.py" />
          </form> <!-- /.select-menu-item -->

      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

          <div class="breadcrumb">
            <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/galicae/bioxsd" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">bioxsd</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/galicae/bioxsd/tree/master/disulfinder" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">disulfinder</span></a></span><span class="separator"> / </span><strong class="final-path">dsToXML.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="disulfinder/dsToXML.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
          </div>
        </div>


        <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/galicae/bioxsd/contributors/master/disulfinder/dsToXML.py">
          Fetching contributors…

          <div class="participation">
            <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
            <p class="loader-error">Cannot retrieve contributors at this time</p>
          </div>
        </div>


        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="octicon octicon-file-text"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>129 lines (101 sloc)</span>
                <span>3.6 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                        <a class="minibutton"
                           href="/galicae/bioxsd/edit/master/disulfinder/dsToXML.py"
                           data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
                  <a href="/galicae/bioxsd/raw/master/disulfinder/dsToXML.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/galicae/bioxsd/blame/master/disulfinder/dsToXML.py" class="button minibutton ">Blame</a>
                  <a href="/galicae/bioxsd/commits/master/disulfinder/dsToXML.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="kn">from</span> <span class="nn">optparse</span> <span class="kn">import</span> <span class="n">OptionParser</span></div><div class='line' id='LC2'><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">defaultdict</span></div><div class='line' id='LC3'><span class="kn">from</span> <span class="nn">lxml.builder</span> <span class="kn">import</span> <span class="n">ElementMaker</span></div><div class='line' id='LC4'><span class="kn">from</span> <span class="nn">lxml</span> <span class="kn">import</span> <span class="n">etree</span> <span class="k">as</span> <span class="n">et</span></div><div class='line' id='LC5'><span class="c">#doto: read from stdin</span></div><div class='line' id='LC6'><span class="k">def</span> <span class="nf">parseDisulfinder</span><span class="p">(</span><span class="n">inFile</span><span class="p">):</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'>	<span class="n">data</span><span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span></div><div class='line' id='LC9'>	<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">inFile</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span></div><div class='line' id='LC10'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">f</span><span class="p">:</span></div><div class='line' id='LC11'>			<span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&quot;Abbreviations&quot;</span><span class="p">):</span></div><div class='line' id='LC12'>				<span class="k">break</span></div><div class='line' id='LC13'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	<span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&quot;AA&quot;</span><span class="p">):</span></div><div class='line' id='LC14'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	<span class="n">data</span><span class="p">[</span><span class="s">&#39;AA&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()))</span></div><div class='line' id='LC15'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	<span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&quot;DB_state&quot;</span><span class="p">)</span> <span class="ow">or</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&quot;DB_conf&quot;</span><span class="p">)</span> <span class="ow">or</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">&quot;DB_flip&quot;</span><span class="p">):</span></div><div class='line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	<span class="n">content</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	<span class="n">lIdent</span> <span class="o">=</span> <span class="n">content</span><span class="p">[:</span><span class="mi">9</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	<span class="n">lData</span> <span class="o">=</span> <span class="n">content</span><span class="p">[</span><span class="mi">9</span><span class="p">:]</span></div><div class='line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	<span class="n">data</span><span class="p">[</span><span class="n">lIdent</span><span class="p">]</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">lData</span><span class="p">))</span></div><div class='line' id='LC20'>	<span class="k">return</span> <span class="n">data</span></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><span class="c">#for key in [&quot;AA&quot;,&quot;DB_state&quot;,&quot;DB_conf&quot;,&quot;DB_flip&quot;]:</span></div><div class='line' id='LC23'><span class="c">#	print key</span></div><div class='line' id='LC24'><span class="c">#	print &quot;&quot;.join(data[key])</span></div><div class='line' id='LC25'><span class="c">#	print len(data[key])</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'><span class="k">def</span> <span class="nf">getContentIds</span><span class="p">(</span><span class="n">data</span><span class="p">):</span></div><div class='line' id='LC28'>	<span class="n">res</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC29'>	<span class="k">for</span> <span class="n">i</span><span class="p">,</span><span class="n">db</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;DB_state&#39;</span><span class="p">]):</span></div><div class='line' id='LC30'>		<span class="k">if</span> <span class="n">db</span> <span class="o">!=</span> <span class="s">&quot; &quot;</span><span class="p">:</span></div><div class='line' id='LC31'>			<span class="n">res</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">)</span></div><div class='line' id='LC32'>	<span class="k">return</span> <span class="n">res</span></div><div class='line' id='LC33'><br/></div><div class='line' id='LC34'><br/></div><div class='line' id='LC35'><span class="k">def</span> <span class="nf">writeBXD</span><span class="p">(</span><span class="n">data</span><span class="p">,</span><span class="n">outFile</span><span class="p">):</span></div><div class='line' id='LC36'>	<span class="n">DI</span> <span class="o">=</span> <span class="s">&quot;http://rostlab.org/disulfinder/output&quot;</span></div><div class='line' id='LC37'>	<span class="n">BX</span> <span class="o">=</span> <span class="s">&quot;http://bioxsd.org/BioXSD-1.1&quot;</span></div><div class='line' id='LC38'>	<span class="n">XSI</span> <span class="o">=</span> <span class="s">&quot;http://www.w3.org/2001/XMLSchema-instance&quot;</span></div><div class='line' id='LC39'>	<span class="n">XS</span> <span class="o">=</span> <span class="s">&quot;{</span><span class="si">%s</span><span class="s">}&quot;</span> <span class="o">%</span> <span class="n">XSI</span></div><div class='line' id='LC40'>	<span class="n">NS_MAP</span> <span class="o">=</span> <span class="p">{</span><span class="s">&quot;di&quot;</span><span class="p">:</span> <span class="n">DI</span><span class="p">,</span> <span class="s">&quot;bx&quot;</span><span class="p">:</span> <span class="n">BX</span><span class="p">,</span> <span class="s">&quot;xsi&quot;</span><span class="p">:</span> <span class="n">XSI</span><span class="p">}</span></div><div class='line' id='LC41'><br/></div><div class='line' id='LC42'>	<span class="n">E</span> <span class="o">=</span> <span class="n">ElementMaker</span><span class="p">(</span><span class="n">namespace</span><span class="o">=</span><span class="n">BX</span><span class="p">,</span> <span class="n">nsmap</span> <span class="o">=</span> <span class="n">NS_MAP</span><span class="p">)</span></div><div class='line' id='LC43'>	<span class="n">DI</span> <span class="o">=</span> <span class="n">ElementMaker</span><span class="p">(</span><span class="n">namespace</span> <span class="o">=</span> <span class="n">DI</span><span class="p">,</span> <span class="n">nsmap</span> <span class="o">=</span> <span class="n">NS_MAP</span><span class="p">)</span></div><div class='line' id='LC44'><br/></div><div class='line' id='LC45'>	<span class="n">flipMap</span> <span class="o">=</span>  <span class="p">{</span> <span class="s">&quot; &quot;</span> <span class="p">:</span> <span class="s">&quot;0&quot;</span> <span class="p">,</span> <span class="s">&quot;*&quot;</span> <span class="p">:</span> <span class="s">&quot;1&quot;</span><span class="p">}</span></div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'>	<span class="n">channel</span> <span class="o">=</span> <span class="n">E</span><span class="o">.</span><span class="n">annotation</span><span class="p">(</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">E</span><span class="o">.</span><span class="n">feature</span><span class="p">(</span></div><div class='line' id='LC49'>				<span class="n">E</span><span class="o">.</span><span class="n">name</span><span class="p">(</span><span class="s">&quot;Cystein disulfide bonding&quot;</span><span class="p">),</span></div><div class='line' id='LC50'>				<span class="n">E</span><span class="o">.</span><span class="n">equalConcept</span><span class="p">(</span><span class="n">term</span><span class="o">=</span><span class="s">&quot;Binary cystein bonding map inside of one chain&quot;</span><span class="p">)</span></div><div class='line' id='LC51'>			<span class="p">),</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">E</span><span class="o">.</span><span class="n">condensedReferences</span><span class="p">(</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">E</span><span class="o">.</span><span class="n">methodIdRef</span><span class="p">(</span><span class="s">&quot;M#di&quot;</span><span class="p">)</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC56'><br/></div><div class='line' id='LC57'><br/></div><div class='line' id='LC58'><br/></div><div class='line' id='LC59'>	<span class="k">for</span> <span class="n">dsID</span> <span class="ow">in</span> <span class="n">getContentIds</span><span class="p">(</span><span class="n">data</span><span class="p">):</span></div><div class='line' id='LC60'>		<span class="n">item</span> <span class="o">=</span> <span class="n">E</span><span class="o">.</span><span class="n">occurrence</span><span class="p">(</span></div><div class='line' id='LC61'>			<span class="n">E</span><span class="o">.</span><span class="n">position</span><span class="p">(</span></div><div class='line' id='LC62'>				<span class="n">E</span><span class="o">.</span><span class="n">point</span><span class="p">({</span><span class="s">&quot;pos&quot;</span> <span class="p">:</span> <span class="nb">str</span><span class="p">(</span><span class="n">dsID</span><span class="p">),</span> <span class="n">XS</span> <span class="o">+</span> <span class="s">&quot;type&quot;</span> <span class="p">:</span> <span class="s">&quot;bx:SequencePoint&quot;</span><span class="p">}),</span></div><div class='line' id='LC63'>				<span class="p">{</span> <span class="n">XS</span> <span class="o">+</span> <span class="s">&quot;type&quot;</span> <span class="p">:</span> <span class="s">&quot;bx:SequencePosition&quot;</span><span class="p">}</span></div><div class='line' id='LC64'>			<span class="p">),</span></div><div class='line' id='LC65'>			<span class="n">E</span><span class="o">.</span><span class="n">score</span><span class="p">(</span></div><div class='line' id='LC66'>				<span class="n">scoreTypeIdRef</span><span class="o">=</span><span class="s">&quot;S#st&quot;</span><span class="p">,</span><span class="n">value</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;DB_state&#39;</span><span class="p">][</span><span class="n">dsID</span><span class="p">])</span></div><div class='line' id='LC67'>			<span class="p">),</span></div><div class='line' id='LC68'>			<span class="n">E</span><span class="o">.</span><span class="n">score</span><span class="p">(</span></div><div class='line' id='LC69'>				<span class="n">scoreTypeIdRef</span><span class="o">=</span><span class="s">&quot;S#co&quot;</span><span class="p">,</span><span class="n">value</span><span class="o">=</span><span class="nb">str</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;DB_conf&#39;</span><span class="p">][</span><span class="n">dsID</span><span class="p">])</span></div><div class='line' id='LC70'>			<span class="p">),</span></div><div class='line' id='LC71'>			<span class="n">E</span><span class="o">.</span><span class="n">score</span><span class="p">(</span></div><div class='line' id='LC72'>				<span class="n">scoreTypeIdRef</span><span class="o">=</span><span class="s">&quot;S#fl&quot;</span><span class="p">,</span><span class="n">value</span><span class="o">=</span><span class="n">flipMap</span><span class="p">[</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;DB_flip&#39;</span><span class="p">][</span><span class="n">dsID</span><span class="p">]]</span></div><div class='line' id='LC73'>			<span class="p">)</span></div><div class='line' id='LC74'>		<span class="p">)</span></div><div class='line' id='LC75'>		<span class="n">channel</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="p">)</span></div><div class='line' id='LC76'><br/></div><div class='line' id='LC77'><br/></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'>	<span class="n">mydoc</span> <span class="o">=</span> <span class="n">DI</span><span class="o">.</span><span class="n">disulfideBridgePrediction</span><span class="p">(</span></div><div class='line' id='LC80'>	<span class="n">E</span><span class="o">.</span><span class="n">referenceSequence</span><span class="p">(</span></div><div class='line' id='LC81'>		<span class="n">E</span><span class="o">.</span><span class="n">sequenceRecord</span><span class="p">(</span></div><div class='line' id='LC82'>			<span class="n">E</span><span class="o">.</span><span class="n">sequence</span><span class="p">(</span><span class="s">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="s">&#39;AA&#39;</span><span class="p">])),{</span><span class="n">XS</span><span class="o">+</span><span class="s">&quot;type&quot;</span> <span class="p">:</span> <span class="s">&quot;bx:GeneralAminoacidSequenceRecord&quot;</span>  <span class="p">}</span></div><div class='line' id='LC83'>		<span class="p">)</span></div><div class='line' id='LC84'>	<span class="p">),</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">E</span><span class="o">.</span><span class="n">blockWithOccurrenceReferences</span><span class="p">(</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">E</span><span class="o">.</span><span class="n">method</span><span class="p">(</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">E</span><span class="o">.</span><span class="n">categoryConcept</span><span class="p">({</span></div><div class='line' id='LC88'>				<span class="s">&quot;accession&quot;</span> <span class="p">:</span> <span class="s">&quot;operation_1850&quot;</span><span class="p">,</span></div><div class='line' id='LC89'>				<span class="s">&quot;conceptUri&quot;</span> <span class="p">:</span> <span class="s">&quot;http://edamontology.org/operation_1850&quot;</span><span class="p">,</span></div><div class='line' id='LC90'>				<span class="s">&quot;ontologyName&quot;</span> <span class="p">:</span> <span class="s">&quot;EDAM&quot;</span><span class="p">,</span></div><div class='line' id='LC91'>				<span class="s">&quot;term&quot;</span> <span class="p">:</span> <span class="s">&quot;Protein cysteine and disulfide bond assignment&quot;</span></div><div class='line' id='LC92'>			<span class="p">}),</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">E</span><span class="o">.</span><span class="n">citation</span><span class="p">(</span><span class="n">date</span><span class="o">=</span><span class="s">&quot;2013-06-28&quot;</span><span class="p">),</span></div><div class='line' id='LC94'>			<span class="n">localId</span><span class="o">=</span><span class="s">&quot;M#di&quot;</span><span class="p">,</span><span class="n">name</span><span class="o">=</span><span class="s">&quot;disulfinder&quot;</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">),</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">E</span><span class="o">.</span><span class="n">scoreType</span><span class="p">(</span><span class="n">localId</span><span class="o">=</span><span class="s">&quot;S#st&quot;</span><span class="p">),</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">E</span><span class="o">.</span><span class="n">scoreType</span><span class="p">(</span><span class="n">localId</span><span class="o">=</span><span class="s">&quot;S#co&quot;</span><span class="p">),</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">E</span><span class="o">.</span><span class="n">scoreType</span><span class="p">(</span><span class="n">localId</span><span class="o">=</span><span class="s">&quot;S#fl&quot;</span><span class="p">),</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">channel</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">),</span></div><div class='line' id='LC103'>	<span class="p">{</span> <span class="n">XS</span><span class="o">+</span><span class="s">&quot;schemaLocation&quot;</span><span class="p">:</span> <span class="s">&quot;http://rostlab.org/disulfinder/output http://i12r-tbl.informatik.tu-muenchen.de/~alex/disulfinder_output.xsd&quot;</span> <span class="p">}</span></div><div class='line' id='LC104'><br/></div><div class='line' id='LC105'>	<span class="p">)</span></div><div class='line' id='LC106'><br/></div><div class='line' id='LC107'>	<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">outFile</span><span class="p">,</span><span class="s">&quot;w+&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">outF</span><span class="p">:</span></div><div class='line' id='LC108'>		<span class="n">outF</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">et</span><span class="o">.</span><span class="n">tostring</span><span class="p">(</span><span class="n">mydoc</span><span class="p">,</span> <span class="n">pretty_print</span><span class="o">=</span><span class="bp">True</span><span class="p">))</span></div><div class='line' id='LC109'><br/></div><div class='line' id='LC110'><br/></div><div class='line' id='LC111'><br/></div><div class='line' id='LC112'><span class="k">def</span> <span class="nf">main</span><span class="p">():</span></div><div class='line' id='LC113'>	<span class="n">parser</span> <span class="o">=</span> <span class="n">OptionParser</span><span class="p">()</span></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'>	<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-i&quot;</span><span class="p">,</span><span class="s">&quot;--input&quot;</span><span class="p">,</span><span class="n">dest</span><span class="o">=</span><span class="s">&quot;inFile&quot;</span><span class="p">,</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	        <span class="n">help</span><span class="o">=</span><span class="s">&quot;disulfinder ascii output file&quot;</span><span class="p">)</span></div><div class='line' id='LC117'>	<span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&quot;-o&quot;</span><span class="p">,</span><span class="s">&quot;--output&quot;</span><span class="p">,</span><span class="n">dest</span><span class="o">=</span><span class="s">&quot;outFile&quot;</span><span class="p">,</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	        <span class="n">help</span><span class="o">=</span><span class="s">&quot;BioXSD conform XML version of the disulfinder output&quot;</span><span class="p">)</span></div><div class='line' id='LC119'><br/></div><div class='line' id='LC120'>	<span class="n">options</span><span class="p">,</span><span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span></div><div class='line' id='LC121'><br/></div><div class='line' id='LC122'>	<span class="n">data</span> <span class="o">=</span> <span class="n">parseDisulfinder</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">inFile</span><span class="p">)</span></div><div class='line' id='LC123'>	<span class="n">writeBXD</span><span class="p">(</span><span class="n">data</span><span class="p">,</span><span class="n">options</span><span class="o">.</span><span class="n">outFile</span><span class="p">)</span></div><div class='line' id='LC124'><br/></div><div class='line' id='LC125'><br/></div><div class='line' id='LC126'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span></div><div class='line' id='LC127'>	<span class="n">main</span><span class="p">()</span></div><div class='line' id='LC128'><br/></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;">
            <button type="submit" class="button">Go</button>
          </form>
        </div>

</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif" height="64" width="64">
</div>


          </div>
        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div>
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">Developer</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>
    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2013 <span title="0.11948s from fe17.rs.github.com">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/galicae/bioxsd/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

    
    <span id='server_response_time' data-time='0.11994' data-host='fe17'></span>
    
  </body>
</html>

