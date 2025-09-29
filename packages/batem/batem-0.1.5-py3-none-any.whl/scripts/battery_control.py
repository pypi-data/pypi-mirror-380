
# Setup Python path before imports

import os
#import scripts.setup_path  # noqa: F401

# import batem.reno
from batem.reno.indicators.models import BasicIndicators, BatteryIndicators


from batem.reno.indicators.evaluation import (
    BatteryPrinter, Printer, calculate_basic_indicators,
    calculate_battery_indicators)
from batem.reno.battery.model import (
    BPINaiveStrategy, Battery, BatteryConfig, BatteryFilePathBuilder,
    BatterySimulationExperiment, BatterySimulationResult,
    CaseBasedReasoningStrategy,
    InactiveNightStrategy, NaiveStrategy, PeriodsStrategy, Phases,
    SeasonsStrategy, Strategy)
from batem.reno.house.creation import HouseBuilder
from batem.reno.house.services import ConsumptionAggregator, ConsumptionTrimmer
from batem.reno.house.model import House
from batem.reno.pv.model import PVPlant
from batem.reno.plot.base import Plotter
from batem.reno.plot.battery import (
    BatteryDataProcessor, BatteryPlotConfig, BatteryRenderer,
    BatteryAxesConfigurator, BatteryFigureSaver,
    InteractiveAxesConfigurator, InteractiveFigureSaver, InteractiveRenderer)
from batem.reno.pv.creation import PVPlantBuilder, WeatherDataBuilder
from batem.reno.utils import TimeSpaceHandler


def simulate_strategy(house: House, pv_plant: PVPlant,
                      battery: Battery):

    for time, consumption in house.consumption.usage_hourly.items():
        production = pv_plant.production.usage_hourly[time]
        battery.step(time, consumption, production)


def generate_report(house: House,
                    pv_plant: PVPlant,
                    battery: Battery) -> tuple[BasicIndicators,
                                               BatteryIndicators]:
    initial_indicators = calculate_basic_indicators(house, pv_plant)
    Printer(initial_indicators).print(prefix="Initial ")
    final_indicators = calculate_battery_indicators(house, pv_plant, battery)
    BatteryPrinter(final_indicators).print(prefix="Final ")
    return initial_indicators, final_indicators


def generate_plots(folder: str,
                   strategy: Strategy,
                   battery: Battery,
                   house: House,
                   pv_plant: PVPlant,
                   initial_indicators: BasicIndicators,
                   final_indicators: BatteryIndicators):

    file_path = os.path.join(folder, f"battery_plot_{strategy.name}.png")
    Plotter(
        config=BatteryPlotConfig(
            file_path=file_path,
            as_png=True,
            size=(10, 5)),
        data_processor=BatteryDataProcessor(),
        renderer=BatteryRenderer(),
        axes_configurator=BatteryAxesConfigurator(),
        figure_saver=BatteryFigureSaver()
    ).plot(BatterySimulationResult(
        battery=battery,
        house=house,
        pv_plant=pv_plant,
        initial_indicators=initial_indicators,
        final_indicators=final_indicators))

    file_path = os.path.join(
        folder, f"battery_plot_interactive_{strategy.name}.html")
    Plotter(
        config=BatteryPlotConfig(
            file_path=f"battery_plot_interactive_{strategy.name}.html",
            as_png=True,
            size=(10, 5)),
        data_processor=BatteryDataProcessor(),
        renderer=InteractiveRenderer(),
        axes_configurator=InteractiveAxesConfigurator(),
        figure_saver=InteractiveFigureSaver()
    ).plot(BatterySimulationResult(
        battery=battery,
        house=house,
        pv_plant=pv_plant,
        initial_indicators=initial_indicators,
        final_indicators=final_indicators))


if __name__ == "__main__":

    # python scripts/battery_control.py

    time_space_handler = TimeSpaceHandler(location="Bucharest",
                                          start_date="01/02/1998",
                                          end_date="01/02/1999")

    house = HouseBuilder().build_house_by_id(2000901)

    weather_data = WeatherDataBuilder().build(
        location=time_space_handler.location,
        latitude_north_deg=time_space_handler.latitude_north_deg,
        longitude_east_deg=time_space_handler.longitude_east_deg,
        from_datetime_string=time_space_handler.start_date,
        to_datetime_string=time_space_handler.end_date)

    pv_plant = PVPlantBuilder().build(weather_data=weather_data,
                                      exposure_deg=0,
                                      slope_deg=160,
                                      number_of_panels=10,
                                      peak_power_kW=5)

    ConsumptionTrimmer(house).trim_consumption_house(time_space_handler)
    house.consumption.usage_hourly = ConsumptionAggregator(
        house).get_total_consumption_hourly()

    battery_config = BatteryConfig(
        capacity_kWh=14,
        max_discharge_power_kW=5,
        max_charge_power_kW=5,
        round_trip_efficiency=0.9)

    for strategy in [
        NaiveStrategy(battery_config),
        InactiveNightStrategy(battery_config),
        PeriodsStrategy(battery_config),
        SeasonsStrategy(battery_config),
        BPINaiveStrategy(battery_config),
        # CaseBasedReasoningStrategy(battery_config,
        #                            Phases.case_based_reasoning)
    ]:
        experiment = BatterySimulationExperiment(
            name=f"battery simulation {strategy.name}",
            battery_config=strategy._config,
            house=house,
            pv_plant=pv_plant)

        battery = Battery(experiment=experiment,
                          strategy=strategy,
                          config=strategy._config)

        simulate_strategy(house, pv_plant, battery)

        if (isinstance(strategy, CaseBasedReasoningStrategy)
                and strategy._phase == Phases.learning):
            print("Exporting cases")
            battery._case_repository.export_cases()

        initial_indicators, final_indicators = generate_report(
            house, pv_plant, battery)
        folder = BatteryFilePathBuilder(
        ).file_path_builder.get_experiment_folder(experiment)
        generate_plots(folder,
                       strategy=strategy,
                       battery=battery,
                       house=house,
                       pv_plant=pv_plant,
                       initial_indicators=initial_indicators,
                       final_indicators=final_indicators)
