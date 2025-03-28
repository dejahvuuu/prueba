import json
import os

class MIOTRansportSystem:
    def __init__(self, data_file="mio_data.json"):
        self.routes = {}  
        self.stops = {}  
        self.data_file = data_file

        self.load_data()

    def save_data(self):
        data = {
            "routes": {route_id: list(stops) for route_id, stops in self.routes.items()},
            "stops": {stop_name: list(routes) for stop_name, routes in self.stops.items()},
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Datos guardados en {self.data_file}")

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.routes = {route_id: set(stops) for route_id, stops in data.get("routes", {}).items()}
                self.stops = {stop_name: set(routes) for stop_name, routes in data.get("stops", {}).items()}
            print(f"Datos cargados desde {self.data_file}")

    def add_route(self, route_id, stop_list):
        self.routes[route_id] = set(stop_list)

        for stop in stop_list:
            if stop not in self.stops:
                self.stops[stop] = set()
            self.stops[stop].add(route_id)

        self.save_data()

    def remove_route(self, route_id):
        if route_id in self.routes:
            for stop in self.routes[route_id]:
                if stop in self.stops:
                    self.stops[stop].remove(route_id)
                    if not self.stops[stop]: 
                        del self.stops[stop]
            del self.routes[route_id]
            self.save_data()

    def add_stop(self, route_id, stop_name):
        if route_id in self.routes:
            self.routes[route_id].add(stop_name)

            if stop_name not in self.stops:
                self.stops[stop_name] = set()
            self.stops[stop_name].add(route_id)

            self.save_data()

    def remove_stop(self, route_id, stop_name):
        if route_id in self.routes and stop_name in self.routes[route_id]:
            self.routes[route_id].remove(stop_name)

            if stop_name in self.stops:
                self.stops[stop_name].remove(route_id)
                if not self.stops[stop_name]:  
                    del self.stops[stop_name]

            self.save_data()

    def get_routes_by_stop(self, stop_name):
        return self.stops.get(stop_name, set())

    def display(self):
        print("Rutas del MIO y sus paradas:")
        for route_id, stops in self.routes.items():
            print(f"Ruta {route_id}: {', '.join(stops)}")


if __name__ == "__main__":

    mio_system = MIOTRansportSystem()

    if not mio_system.routes:
        mio_system.add_route("A01", ["Universidades", "Capri", "San Bosco", "Torre de Cali"])
        mio_system.add_route("A02", ["Unidad Deportiva", "Plaza de Toros", "Pampalinda", "Cañaveralejo"])
        mio_system.add_route("A03", ["San Pascual", "Petecuy", "Versalles", "Torre de Cali"])
        mio_system.add_route("A04", ["Nuevo Latir", "Andrés Sanín", "Manzanares", "7 de Agosto"])

    mio_system.display()

    print("\nRutas que pasan por la parada 'Torre de Cali':", mio_system.get_routes_by_stop("Torre de Cali"))

    mio_system.add_stop("A01", "Flora Industrial")
    print("\nDespués de agregar la parada 'Flora Industrial' a la ruta A01:")
    mio_system.display()

    mio_system.remove_stop("A02", "Pampalinda")
    print("\nDespués de eliminar la parada 'Pampalinda' de la ruta A02:")
    mio_system.display()

    mio_system.remove_route("A03")
    print("\nDespués de eliminar la ruta A03:")
    mio_system.display()

    print("\nRutas que pasan por la parada 'San Bosco':", mio_system.get_routes_by_stop("San Bosco"))
