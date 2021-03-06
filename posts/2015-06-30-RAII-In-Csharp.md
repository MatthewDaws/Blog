---
layout: post
title: RAII in C#/Java?
---

More a note to a future self than aything else...  In C++ we have the notion of [Resource Acquisition Is Initialization](https://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization) which I think I have internalised as the following:

> Any "resource" (memory, file, handle etc.) should be "owned" by an object.  An object's constructor should allocate the resource, and the destructor should free the resource (with some appropriate choices then made for what copy/move constructors/assignments should do).  By use of C++11 `unique_ptr` and `shared_ptr` this model can be extended to pointers.

<!--more-->

Notice I didn't mention "exception", though one major additional use of RAII is exception safety: if an exception is thrown, then all objects currently in scope will have their destructors run, and so any resources will be safely released.

In C#/Java we have garbage collection.  This takes care of memory, but not any other "resource".  In C# there is the `IDisposable` interface, and I was for a while confused by what this did.  I am not alone, judging from SO:

   - [Does disposing streamreader close the stream?](http://stackoverflow.com/questions/1065168/does-disposing-streamreader-close-the-stream)
   - [Class Destructor Problem](http://stackoverflow.com/questions/2529222/class-destructor-problem)
   - [What is the difference between using IDisposable vs a destructor in C#?](http://stackoverflow.com/questions/339063/what-is-the-difference-between-using-idisposable-vs-a-destructor-in-c?rq=1)
   - [How do you manage deterministic finalization in C#?](http://stackoverflow.com/questions/188473/how-do-you-manage-deterministic-finalization-in-c)
   
For me, the following is a good way to think:

   - Imagine going back to programming in C.  You allocate memory with `malloc` and then free it later with `free`.  Similarly, if you open a file, you need to later close it.
   - A managed language (let's say C#) removes the need to `free` anything.  But it does _nothing_ for the file open/close issue.
   - So we must manually `close()` a file, say.
   - How then to handle exceptions?  Use the `try ... catch ... finally` idiom!
   - Then the `IDisposable` interface in C# should be thought of as enabling the syntactic sugar of the `using` command.  Similarly the `AutoCloseable` interface in Java 7.
   
What of destructors?  Don't use them: they are only of use if you need to free "unmanaged resources", and if you need to do that, you'll know it.

So why the "IDisposable pattern"?  This seems really to exist merely to support finalizers (aka destructors).  However, if your class is not sealed, then maybe a derived class will need a destructor.  The pattern then exists to ensure unmanaged resources are always freed, but from the destructor no managed resource is freed (as they might have already been freed by the garbage collector).

   - To use inheritance, we must [remember to call the base class `dispose` method](https://msdn.microsoft.com/en-us/library/ms182330.aspx)
   - "Freeing managed resources" amounts to calling `dispose` on member fields, which is the way to handle "composition".
   
All in all, that seems about as much work as writing a destructor in C++!