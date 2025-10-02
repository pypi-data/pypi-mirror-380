import inspect

from .helper_functions import Helper


class InterfaceMeta(type):
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        cls._is_interface_ = getattr(cls, "_is_interface_", None)
        cls._interface_contracts_ = {}
        
        annotations = namespace.get('__annotations__', {})
        for ann_attr, _ in annotations.items():
            if ann_attr not in namespace:
                cls._interface_contracts_[ann_attr] = "field"
        
        return cls

    def __call__(cls, *args, **kwargs):
        if getattr(cls, "_is_interface_", False):
            raise TypeError(f"Cannot instantiate interface class '{cls.__name__}'")
        return super().__call__(*args, **kwargs)
    

    def __validate__(cls):
        if cls._is_interface_ is None:
            raise TypeError("Class must be decorated with @interface or @concrete")

        if cls._is_interface_:
            # enforce interface contracts
            for attr, value in list(vars(cls).items()):
                if attr.startswith("__") and attr.endswith("__"):
                    continue
                if attr in ("__annotations__", "_is_interface_", "_interface_contracts_"):
                    continue

                # ---- METHODS ----
                if inspect.isfunction(value):
                    if not Helper.is_empty_function(value):
                        raise TypeError(
                            f"Method '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    cls._interface_contracts_[attr] = "method"
                    continue

                if isinstance(value, staticmethod):
                    if not Helper.is_empty_function(value.__func__):
                        raise TypeError(
                            f"Static method '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    cls._interface_contracts_[attr] = "method"
                    continue

                if isinstance(value, classmethod):
                    if not Helper.is_empty_function(value.__func__):
                        raise TypeError(
                            f"Class method '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    cls._interface_contracts_[attr] = "method"
                    continue

                # ---- PROPERTY ----
                if isinstance(value, property):
                    errors: list[str] = []
                    if not any([value.fget, value.fset, value.fdel]):
                        errors.append(
                            f"Property '{attr}' in interface '{cls.__name__}' must define at least "
                            "a getter, setter or deleter (even if empty)."
                        )
                    if value.fget is not None and not Helper.is_empty_function(value.fget):
                        errors.append(
                            f"Property getter '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    if value.fset is not None and not Helper.is_empty_function(value.fset):
                        errors.append(
                            f"Property setter '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    if value.fdel is not None and not Helper.is_empty_function(value.fdel):
                        errors.append(
                            f"Property deleter '{attr}' in interface '{cls.__name__}' must have empty body."
                        )
                    if errors:
                        raise TypeError("\n".join(errors))
                    cls._interface_contracts_[attr] = "method"
                    continue

                # ---- FIELD PLACEHOLDER ----
                ann = cls.__annotations__.get(attr) if hasattr(cls, "__annotations__") else None
                if ann is not None:
                    if value is Ellipsis:
                        cls._interface_contracts_[attr] = "field"
                        continue
                    if attr not in cls.__dict__:
                        cls._interface_contracts_[attr] = "field"
                        continue

                if value is Ellipsis:
                    cls._interface_contracts_[attr] = "field"
                    continue

                raise TypeError(
                    f"Attribute '{attr}' in interface '{cls.__name__}' should not have a concrete value."
                )

            # inherit contracts from parents
            for base in cls.__mro__[1:]:
                if hasattr(base, "_interface_contracts_"):
                    cls._interface_contracts_.update(base._interface_contracts_)

        else:
            # enforce concrete implementation
            contracts: dict[str, str] = {}
            for base in cls.__mro__[1:]:
                if hasattr(base, "_interface_contracts_"):
                    contracts.update(base._interface_contracts_)

            missing = []
            for name, kind in contracts.items():
                if kind == "method":
                    impl = getattr(cls, name, None)
                    if impl is None or Helper.is_empty_function(impl):
                        missing.append(name)
                elif kind == "field":
                    if not hasattr(cls, name):
                        missing.append(name)
                    else:
                        val = getattr(cls, name)
                        if val is Ellipsis:
                            missing.append(name)

            if missing:
                raise TypeError(
                    f"Concrete class '{cls.__name__}' must implement contracts: {', '.join(missing)}"
                )
