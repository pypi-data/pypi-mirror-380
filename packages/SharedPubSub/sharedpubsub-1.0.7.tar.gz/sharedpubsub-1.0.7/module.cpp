#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/iostream.h>
#include "SharedPubSub.hpp"
#include "FixedString.h"
#include "Examples.h"

using namespace std;

namespace py = pybind11;


// Utility to deduce remove the atomic part of a type
template<typename T>
struct remove_atomic { using type = T; };                   // Utility type 1 to deduce non-atomic

template<typename U>
struct remove_atomic<std::atomic<U>> { using type = U; };   // Utility type 2 to deduce non-atomic

template<typename T>
using remove_atomic_t = typename remove_atomic<T>::type;    // Utility type 3 to deduce non-atomic

// Publisher overload, U&& doesn't work here, we need const&
template<typename T>
void publisher_setValue(shps::Publisher<T>& pub, const remove_atomic_t<T>& value) { pub.setValue(value); }
template<typename T>
void publisher_publish(shps::Publisher<T>& pub, const remove_atomic_t<T>& value) { pub.publish(value); }
template<typename T>
void publisher_push(shps::Publisher<T>& pub, const remove_atomic_t<T>& value) { pub.push(value); }
template<typename T>
void publisher_setValueAndPush(shps::Publisher<T>& pub, const remove_atomic_t<T>& value) { pub.setValueAndPush(value); }
template<typename T>
void publisher_publishOnChange(shps::Publisher<T>& pub, const remove_atomic_t<T>& value) { pub.publishOnChange(value); }
template<typename T>
void publisher_setValueAndNotifyOnChange(shps::Publisher<T>& pub, const remove_atomic_t<T>& value) { pub.setValueAndNotifyOnChange(value); }


// Subscriber overload, we need to handle timeouts
template<typename T>
std::optional<remove_atomic_t<T>> subscriber_readWait(shps::Subscriber<T>& sub) {
    py::gil_scoped_release release;
    return sub.readWait();
}

template<typename T>
std::optional<remove_atomic_t<T>> subscriber_readWait_timeout(shps::Subscriber<T>& sub, long long timeout) {
    py::gil_scoped_release release;
    return sub.readWait(chrono::milliseconds(timeout));
}

template<typename T>
void subscriber_waitForNotify(shps::Subscriber<T>& sub) {
    py::gil_scoped_release release;
    sub.waitForNotify();
    return;
}

template<typename T>
void subscriber_waitForNotify_timeout(shps::Subscriber<T>& sub, long long timeout) {
    py::gil_scoped_release release;
    sub.waitForNotify(chrono::milliseconds(timeout));
    return;
}

// Templated class declaration to be able to input any types
template<typename T>
void declarePublisher(py::module_ &m, const char* name) {
    py::class_<shps::Publisher<T>>(m, name)
        .def(py::init<const std::string&>())
        .def("rawValue", &shps::Publisher<T>::rawValue, py::return_value_policy::reference)
        .def("setValue", &publisher_setValue<T>)
        .def("readValue", &shps::Publisher<T>::readValue)
        .def("publish", &publisher_publish<T>)
        .def("push", &publisher_push<T>)
        .def("setValueAndPush", &publisher_setValueAndPush<T>)
        .def("publishOnChange", &publisher_publishOnChange<T>)
        .def("setValueAndNotifyOnChange", &publisher_setValueAndNotifyOnChange<T>)
        .def("notifyAll", &shps::Publisher<T>::notifyAll);
}

template<typename T>
void declareSubscriber(py::module_ &m, const char* name) {
    py::class_<shps::Subscriber<T>>(m, name)
        .def(py::init<const std::string&, const std::string&, bool>())
        .def("subscribe", &shps::Subscriber<T>::subscribe)
        .def("clearQueue", &shps::Subscriber<T>::clearQueue)
        .def("rawValue", &shps::Subscriber<T>::rawValue, py::return_value_policy::reference)
        .def("readValue", &shps::Subscriber<T>::readValue)
        .def("readWait", &subscriber_readWait<T>)
        .def("readWaitMS", &subscriber_readWait_timeout<T>, py::arg("timeout"))
        .def("waitForNotify", &subscriber_waitForNotify<T>)
        .def("waitForNotifyMS", &subscriber_waitForNotify_timeout<T>, py::arg("timeout"));
}


// Macro to define both normal and atomic class
#define DECLARE_WITH_ATOMIC(T, name) \
    declarePublisher<T>(m, "Publisher_" name); \
    declareSubscriber<T>(m, "Subscriber_" name); \
    declarePublisher<atomic<T>>(m, "Publisher_atomic_" name); \
    declareSubscriber<atomic<T>>(m, "Subscriber_atomic_" name);

#define DECLARE(T, name) \
    declarePublisher<T>(m, "Publisher_" name); \
    declareSubscriber<T>(m, "Subscriber_" name); 

// Module creation
PYBIND11_MODULE(SharedPubSub, m) {
    // Base types
    DECLARE_WITH_ATOMIC(bool,      "bool")
    DECLARE_WITH_ATOMIC(int,       "int")
    DECLARE_WITH_ATOMIC(uint,      "uint")
    DECLARE_WITH_ATOMIC(int8_t,    "int8")
    DECLARE_WITH_ATOMIC(uint8_t,   "uint8")
    DECLARE_WITH_ATOMIC(int16_t,   "int16")
    DECLARE_WITH_ATOMIC(uint16_t,  "uint16")
    DECLARE_WITH_ATOMIC(int64_t,   "int64")
    DECLARE_WITH_ATOMIC(uint64_t,  "uint64")
    DECLARE_WITH_ATOMIC(float,     "float")
    DECLARE_WITH_ATOMIC(double,    "double")

    // Custom Types
    py::class_<FixedString<2048>>(m, "FixedString2048")
        .def(py::init<>())
        .def(py::init<string>())
        .def("get", &FixedString<2048>::get)
        .def("set", static_cast<void (FixedString<2048>::*)(const string)>(&FixedString<2048>::set))
        .def("size", &FixedString<2048>::size);
    DECLARE(FixedString<2048>, "FixedString2048")

    py::class_<ExampleClass>(m, "ExampleClass")
        .def(py::init<>())
        .def_readwrite("value1", &ExampleClass::value1)
        .def_readwrite("value2", &ExampleClass::value2)
        .def_readwrite("value3", &ExampleClass::value3)
        .def("printValues",&ExampleClass::printValues);
    DECLARE(ExampleClass,"ExampleClass")

    py::class_<ExampleClassAtomic>(m, "ExampleClassAtomic")
        .def(py::init<>())
        .def("getValue1", &ExampleClassAtomic::getValue1)
        .def("getValue2", &ExampleClassAtomic::getValue2)
        .def("getValue3", &ExampleClassAtomic::getValue3)
        .def("setValue1", &ExampleClassAtomic::setValue1)
        .def("setValue2", &ExampleClassAtomic::setValue2)
        .def("setValue3", &ExampleClassAtomic::setValue3)
        .def("printValues",&ExampleClassAtomic::printValues);
    DECLARE(ExampleClassAtomic,"ExampleClassAtomic")
}
