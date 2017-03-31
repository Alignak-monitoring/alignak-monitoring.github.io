---
layout: post
title: "Big rework alignak"
date: 2016-05-10 08:21:50
categories: code
---

Sebastien Coavoux and David Durieux has worked hard these last weeks in Alignak and they have made these modifications:

* Use uuid in all objects instead of id
* Unlink almost all items: attribute of object are no instance of other objects except for a few cases (commandcall / check_period and acknowledgement)
* Replace pickle by manual serialization: return a json representation of objects.
* Drop of base64 / zlib manual serialisation in HTTP and use CherryPy facilities to have json
* Rework class inheritance: instantiation of object is more generic
* Clean unused functions and class
* Increase CherryPy queue for larger environment


So you can ask, is it better?

YES it is!

We have better code, more readable and better performances to serialize and send to other daemons (win between 10 to 50% of time, CPU and memory).

You will be able to see the difference in next release of Alignak ;)
